#!/bin/bash
#SBATCH -n 1
#SBATCH --qos=batch
#SBATCH -e slurm-error.txt
#SBATCH --time=00:120:00

. /fs/cliphomes/dpeskov/anaconda3/bin/activate asr
python  QBASR_GenerateData.py -n {{process_id}}
