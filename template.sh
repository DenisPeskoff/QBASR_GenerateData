#!/bin/bash
#SBATCH -n 1
#SBATCH --qos=dque
#SBATCH -e slurm_error.txt
#SBATCH --time=00:60:00

. /fs/cliphomes/dpeskov/anaconda3/bin/activate asr
python  QBASR_GenerateData.py -n {{process_id}}
