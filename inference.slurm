#!/usr/bin/bash
#SBATCH --partition=short
#SBATCH --account=ie-idi
#SBATCH --time=23:00:00
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --gres=gpu:P100:1
#SBATCH --cpus-per-task=24
#SBATCH --mem=20000
#SBATCH --job-name=infer:)
#SBATCH --output=infer.out
#SBATCH --mail-user=augustab@stud.ntnu.no
#SBATCH --mail-type=ALL

WORKDIR=${SLURM_SUBMIT_DIR}
cd ${WORKDIR}
echo "we are running from this directory: $SLURM_SUBMIT_DIR"
echo " the name of the job is: $SLURM_JOB_NAME"
echo "Th job ID is $SLURM_JOB_ID"
echo "The job was run on these nodes: $SLURM_JOB_NODELIST"
echo "Number of nodes: $SLURM_JOB_NUM_NODES"
echo "We are using $SLURM_CPUS_ON_NODE cores"
echo "We are using $SLURM_CPUS_ON_NODE cores per node"
echo "Total of $SLURM_NTASKS cores"

module purge
module load Anaconda3/2020.07
echo "anaconda loaded"

pip3 install -r requirements.txt --user -q
echo "pip install succsess"

python detect.py --source ../../../../projects/vc/courses/TDT17/2022/open/RDD2022/Norway/test/images/ --data dataset_nowjap.yaml --weights ./runs/train/nowjap3/weights/best.pt --conf-thres 0.192 --max-det 5 --name nowjap06 --save-txt --img 1302 --iou-thres 0.65

uname --a
