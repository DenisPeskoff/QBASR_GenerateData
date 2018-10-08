import argparse
import os

def split(input_file, output_dir, total_chunks=2):
    with open(input_file, 'r') as fp:
        max_i = len(fp)/total_chunks
        file_chunk = 0
        i = 0
        for line in fp:
            i +=1
            #reset if new chunk is needed
            if i == max_i:
                file_chunk += 1
                i = 0
            # you need i from total_chunks
            with open(os.path.join(output_dir, 'chunk{file_chunk}.json'), 'w') as o:
                o.write(line)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('-t', dest='total_chunks', help='Total number of chunks', default=2, type=int)
    parser.add_argument('-i', dest='input_file', help='File to split')
    parser.add_argument('-o', dest='output_dir', help='Directory to dump chunks into')
    args = parser.parse_args()

    split(args.input_file, args.output_dir, args.total_chunks)
