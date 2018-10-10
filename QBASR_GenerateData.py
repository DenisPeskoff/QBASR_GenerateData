from gtts import gTTS

import subprocess
import argparse
import json
import glob
import time
import sys


#This script generates Audio Data from QuizBowl questions, leveraging Google's Text to Speech API
def run(process_id):

    #load all relevant data for the chunk
    with open(f'chunk{process_id}.json') as fp:
        data = json.load(fp)

    questions = data['questions']

    #extract all the relevant questions for given fold
    buzzer_data = []
    for question in data['questions']:
        if question['fold'] == 'buzzertrain':
            buzzer_data.append([question['sentences'], question['page'], question['qnum']])

    #extract relevant information from format
    data = []
    for index, sentences in enumerate([x[0] for x in buzzer_data]):
        for sent_count, sentence in enumerate(sentences):
            data.append([buzzer_data[index][2], sent_count, sentence, buzzer_data[index][1]])

    #convert all the data into speech and save it
    for sentence in data:
        file_name = str(sentence[0]) + "_" + str(sentence[1])
        text = sentence[2]
        # convert into audio with gTTS, save it to mp3, convert it to WAV
        try:
            sentTTS = gTTS(text, lang='en', slow=False)
            sentTTS.save('/fs/clip-quiz/dpeskov/data/' + file_name + ".mp3")

        #sometimes the API might get overwhelmed, take a break then try again
        except:
            print("sleeping")
            time.sleep(3)
            sentTTS = gTTS(text, lang='en', slow=False)
            sentTTS.save('/fs/clip-quiz/dpeskov/guesser_mp3/' + file_name + ".mp3")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument('-n', dest='process_id', help='Process ID (used to split files)', default=0, type=int)
    # parser.add_argument('-t', dest='total_processes', help='Total number of processes', default=1, type=int)
    args = parser.parse_args()

    # if args.process_id >= args.total_processes:
    #     print('Invalid process id')
    #     sys.exit(0)

    run(args.process_id)