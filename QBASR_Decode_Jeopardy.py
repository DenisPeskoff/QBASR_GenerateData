import subprocess
import argparse
import os
import glob

def run(process_id):

    location = "jeopardy/all"

    generated = glob.glob(f'/fs/clip-quiz/dpeskov/data/{location}/base_lattices/*.lat')
    try:
       os.mkdir(f"/fs/clip-quiz/dpeskov/data/{location}/base_wav")
       os.mkdir(f"/fs/clip-quiz/dpeskov/data/{location}/base_lattices")
    except:
        pass    

    with open(f'output_dir/chunk{process_id}') as fp:
        file_list = fp.readlines()

    os.chdir('/fs/clip-sw/user-supported/kaldi/egs/aspire/s5')
    transcriptions = {}
    for each_file in file_list:
        each_file = each_file.strip()
        file_name = each_file[each_file.rfind('/') + 1:each_file.rfind('.')]
        file_name_mp3 = file_name + ".mp3"
        file_name_wav = f"/fs/clip-quiz/dpeskov/data/{location}/base_wav/" + file_name + ".wav"
        # file_name_edit = "wav_edit/"+file_name+"_edit.wav"
        file_name_lat = f"/fs/clip-quiz/dpeskov/data/{location}/base_lattices/" + file_name + ".lat"

        #in case the data generation did not finish, skip previously generated instances
        if file_name_lat in generated:
            continue

        # convert mp3 to a specific Kaldi-friendly wave
        #args = ['/opt/local/stow/ffmpeg-2.7.1/bin/ffmpeg','-y','-i',each_file, '-acodec', 'pcm_s16le', '-ac', '1', '-ar','8000',file_name_wav]
        args = f"/opt/local/stow/ffmpeg-2.7.1/bin/ffmpeg -y -i {each_file} -acodec pcm_s16le -ac 1 -ar 8000 {file_name_wav}"
        discard_output = subprocess.run( args, shell = True)

        subprocess.run('pwd')
        subprocess.call('. cmd.sh', shell = True)
        subprocess.call('. path.sh', shell = True)
        # Kaldi
        #args = ['online2-wav-nnet3-latgen-faster','--online=false', '--do-endpointing=false ', '--frame-subsampling-factor=3', '--config=exp/tdnn_7b_chain_online/conf/online.conf' , '--max-active=7000', '--beam=15.0', '--lattice-beam=6.0', '--acoustic-scale=1.0', '--word-symbol-table=exp/tdnn_7b_chain_online/graph_pp/words.txt', 'exp/tdnn_7b_chain_online/final.mdl', 'exp/tdnn_7b_chain_online/graph_pp/HCLG.fst', 'ark:echo', 'utterance-id1', ' utterance-id1|', 'scp:echo', 'utterance-id1', f'{file_name_wav}|', f'ark,t:{file_name_lat}']
        
        args = f"online2-wav-nnet3-latgen-faster \
        --online=false \
        --do-endpointing=false \
          --frame-subsampling-factor=3 \
          --config=exp/tdnn_7b_chain_online/conf/online.conf \
          --max-active=7000 \
          --beam=15.0 \
          --lattice-beam=6.0 \
          --acoustic-scale=1.0 \
          --word-symbol-table=exp/tdnn_7b_chain_online/graph_pp/words.txt \
          exp/tdnn_7b_chain_online/final.mdl \
	  exp/tdnn_7b_chain_online/graph_pp/HCLG.fst \
          'ark:echo utterance-id1 utterance-id1|' \
          'scp:echo utterance-id1 {file_name_wav}|' \
          'ark,t:{file_name_lat}'"
        output_kaldi  = subprocess.run( args, shell = True)
        #transcriptions[file_name] = output_kaldi[7][14:]
        #with open('/fs/clip-quiz/dpeskov/QBASR_GenerateData/output', 'w') as f:
        #     f.write(transcriptions)
	#maybe dump this, but probably not needed
        print ("Sucess! Finished Job")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument('-n', dest='process_id', help='Process ID (used to split files)', default=0, type=int)
    args = parser.parse_args()
    run(args.process_id)
                                
