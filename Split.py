import argparse
import os
import json

def split(input_file, output_dir, total_chunks=2):
    with open(input_file, 'r') as fp:
        data = json.load(fp)
        questions = data['questions']
        max_i = int(len(questions)/total_chunks)
        print(max_i)
        file_chunk, i = 1, 0
        temp_store = []
        for line in questions:
            i+=1
            temp_store.append(line)
            #reset if new chunk is needed
            if i == max_i:
                i = 0
                with open(os.path.join(output_dir, f'chunk{file_chunk}.json'), 'w') as o:
                    #for line in temp_store:
                    json.dump({"questions":temp_store}, o)
                temp_store = []
                file_chunk += 1

        # last chunk is slightly smaller
        if temp_store:
            with open(os.path.join(output_dir, 'chunk{file_chunk}.json'.format(file_chunk=file_chunk)), 'w') as o:
                json.dump({"questions":temp_store}, o)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('-t', dest='total_chunks', help='Total number of chunks', default=2, type=int)
    parser.add_argument('-i', dest='input_file', help='File to split')
    parser.add_argument('-o', dest='output_dir', help='Directory to dump chunks into')
    args = parser.parse_args()

    split(args.input_file, args.output_dir, args.total_chunks)
