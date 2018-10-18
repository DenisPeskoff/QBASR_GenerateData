import argparse
import os
import math

def split(input_file, output_dir, total_chunks=2):
    with open(input_file, 'r') as fp:
        data = fp.readlines()
        max_i = math.ceil(len(data)/total_chunks)
        #if len(data)%total_chunks != 0:
        #     lower_flag = True
        #else:
        #     lower_flag = False


        print("Splitting into sections of ", max_i)
        file_chunk, i = 1, 0
        temp_store = []
        for line in data:
            i+=1
            temp_store.append(line)
            #reset if new chunk is needed
            if i == max_i:
                i = 0
                with open(os.path.join(output_dir, f'chunk{file_chunk}'), 'w') as o:
                    #for line in temp_store:
                    o.write("".join(temp_store))  

                temp_store = []
                #halfway through lower the ceiling by 1 for equally spaced data
                #if file_chunk >= (total_chunks/2) and lower_flag:
                #    max_i = max_i-1
                #    lower_flag = False
                file_chunk += 1
        # last chunk is slightly smaller
        if temp_store:
             with open(os.path.join(output_dir, 'chunk{file_chunk}'.format(file_chunk=file_chunk)), 'w') as o:
                o.write("".join(temp_store))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('-t', dest='total_chunks', help='Total number of chunks', default=2, type=int)
    parser.add_argument('-i', dest='input_file', help='File to split')
    parser.add_argument('-o', dest='output_dir', help='Directory to dump chunks into')
    args = parser.parse_args()

    split(args.input_file, args.output_dir, args.total_chunks)
