mkdir output_dir
mkdir submissions

python Split.py -t $1 -i data.json -o output_dir/

for i in $(seq $1) 
do
    cp template.sh submissions/submit${i}.sh
    sed -i "s/{{process_id}}/${i}/g" submissions/submit${i}.sh
    sbatch submissions/submit${i}.sh
done

# submit.sh 8
