
def run(process_id):

    with open(f'chunk{process_id}.json') as fp:
        file_list = json.load(fp)

    for each_file in file_list:
        file_name = each_file[each_file.rfind('/') + 1:each_file.rfind('.')]
        file_name_mp3 = file_name + ".mp3"
        file_name_wav = "/fs/clip-quiz/dpeskov/buzzer_data/wav/" + file_name + ".wav"
        # file_name_edit = "wav_edit/"+file_name+"_edit.wav"
        file_name_lat = "/fs/clip-quiz/dpeskov/nounk_lattices/" + file_name + ".lat"

        # convert mp3 to a specific Kaldi-friendly wav
        # discard_output = !/opt/local/stow/ffmpeg-1.2/bin/ffmpeg -y -i {each_file} -acodec pcm_s16le -ac 1 -ar 8000 {file_name_wav}

        # Kaldi
        output_kaldi = !online2 - wav - nnet3 - latgen - faster \- -online = false \
                                                                             - -do - endpointing = false \
                                                                                                   - -frame - subsampling - factor = 3 \
                                                                                                                                     - -config = exp / tdnn_7b_chain_online / conf / online.conf \
                                                                                                                                                 - -max - active = 7000 \
                                                                                                                                                                   - -beam = 15.0 \
                                                                                                                                                                             - -lattice - beam = 6.0 \
                                                                                                                                                                                                 - -acoustic - scale = 1.0 \
                                                                                                                                                                                                                       - -word - symbol - table = exp / tdnn_7b_chain_online / graph_pp / words.txt \
                exp / tdnn_7b_chain_online / final.mdl \
                exp / tdnn_7b_chain_online / graph_pp / no_unks.fst \
                'ark:echo utterance-id1 utterance-id1|' \
                'scp:echo utterance-id1 {file_name_wav}|' \
                'ark,t:{file_name_lat}'

        transcriptions[file_name] = output_kaldi[7][14:]
        #maybe dump this, but probably not needed