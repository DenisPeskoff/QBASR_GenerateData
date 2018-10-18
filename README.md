# QBASR_GenerateData

The following document allows you to Slurm documents.  There are two parts.

## Part 1: Audio Generation
This includes submit.sh, template.sh, QBASR_GenerateData.py
1)Add file in proper json format from https://sites.google.com/view/qanta/datasets?authuser=0
2)Update QBASR_GenerateData to save in the right place
3)Update template.sh to refer to the proper anaconda path, file, etc.
4)Run "submit.sh 48" (or appropriate amount of partitions)

## Part 2: Decoding
This includes submit_decode.sh, template_decode.sh, QBASR_GenerateFileList, QBASR_DecodeAudio.py
Depends on kaldi installation and ffmpeg (to make .wav files from .mp3s)
1) Run QBASR_GenerateFileList on the proper folder e.g. "/dev/*.mp3"
2) Update template.sh to refer to proper file and DecodeAudio to write to correct location
3) Run submit_decode.sh
