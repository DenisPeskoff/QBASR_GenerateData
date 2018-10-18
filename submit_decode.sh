mkdir output_dir
mkdir submissions

python Split_decode.py -t $1 -i qanta.train.filelist -o output_dir/

for i in $(seq $1)
do
    cp template_decode.sh submissions/submit${i}.sh
    sed -i "s/{{process_id}}/${i}/g" submissions/submit${i}.sh
    sbatch submissions/submit${i}.sh
done

