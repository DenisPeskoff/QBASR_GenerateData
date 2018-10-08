import glob
import sys


#folder path should look like: '/fs/clip-scratch/dpeskov/guesser_mp3/*.mp3'
def generate_filelist(folder_path):

     # this isn't needed but clip project space breaks on glob sometimes
    file_list = []
    for each_file in (glob.glob(folder_path)):
        file_list.append(each_file)

    file_list = file_list.sort(key=lambda file: int(file[file.rfind('/') + 1:file.rfind('_')]))

    with open('ASR_FileList', 'w') as f:
        for each_file in file_list:
            f.write(each_file)


if __name__ == "__main__":
    generate_filelist(sys.argv[1])