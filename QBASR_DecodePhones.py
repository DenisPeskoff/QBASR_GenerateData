import subprocess
import argparse
import os
import re

def run(process_id):

    with open(f'output_dir/chunk{process_id}') as fp:
        file_list = fp.readlines()
        
    folder = re.compile('lattices')

    for each_file in file_list:
        each_file = each_file.strip()
        write_location = folder.sub('phones_lattices',each_file[:each_file.rfind('.')])+".lat"
        args = f"/fs/clip-sw/user-supported/kaldi/src/latbin/lattice-to-phone-lattice /fs/clip-sw/user-supported/kaldi/egs/aspire/s5/exp/tdnn_7b_chain_online/final.mdl ark:{each_file} ark,t:{write_location}"
        output_kaldi  = subprocess.run( args, shell = True)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument('-n', dest='process_id', help='Process ID (used to split files)', default=0, type=int)
    args = parser.parse_args()
    run(args.process_id)
                            
