from gtts import gTTS
import subprocess
import argparse
import json
import glob
import time
import sys

location = "all"

generated = glob.glob(f'/fs/clip-quiz/dpeskov/data/jeopardy/all')

#This script generates Audio Data from QuizBowl questions, leveraging Google's Text to Speech API
def run(process_id):

    #load all relevant data for the chunk
    with open(f'output_dir/chunk{process_id}.json') as fp:
        data = json.load(fp)

    questions = data
    guesser_data = []
    for question in questions['questions']:
        # extract all the relevant questions for given fold
        guesser_data.append([question['question'],  question['category'], question['answer'], question['qnum']])
    #extract relevant information from format
    data = []

    #break up the question into individual sentences
    for text, category, page, qnum in guesser_data:
        data.append([qnum, category,text, page])
            #data.append([buzzer_data[index][3], sent_count, sentence, buzzer_data[index][1]])
    sleep_count = 0
    #convert all the data into speech and save it
    for sentence in data:
        file_name = str(sentence[0])
        text = sentence[2]
        # convert into audio with gTTS, save it to mp3, convert it to WAV
        
        if f'/fs/clip-quiz/dpeskov/data/jeopardy/all/{file_name}.mp3' in generated:
            continue

        if not text:
           print (f'Issue with {file_name}')
           continue

        try:
            sentTTS = gTTS(text, lang='en', slow=False)
            sentTTS.save(f'/fs/clip-quiz/dpeskov/data/jeopardy/all/{file_name}.mp3')

        #sometimes the API might get overwhelmed, take a break then try again
        except:
            try:
               sleep_count += 1
               print("sleeping")
               time.sleep(5)
               sentTTS = gTTS(text, lang='en', slow=False)
               sentTTS.save(f'/fs/clip-quiz/dpeskov/data/jeopardy/all/{file_name}.mp3')
            except:
               print (f'Issue with {file_name} .  The data is: {text}')

    print ("Sucess! Finished Job")
    print (f"Slept {sleep_count} times")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument('-n', dest='process_id', help='Process ID (used to split files)', default=0, type=int)
    # parser.add_argument('-t', dest='total_processes', help='Total number of processes', default=1, type=int)
    args = parser.parse_args()

    # if args.process_id >= args.total_processes:
    #     print('Invalid process id')
    #     sys.exit(0)

    run(args.process_id)
