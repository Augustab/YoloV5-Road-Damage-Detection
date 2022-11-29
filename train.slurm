#!/usr/bin/bash
#SBATCH --partition=GPUQ
#SBATCH --account=ie-idi
#SBATCH --time=23:00:00
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --gres=gpu:A100m40:1
#SBATCH --cpus-per-task=24
#SBATCH --mem=50000
#SBATCH --job-name=nissefar
#SBATCH --output=saturday.out
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

python train.py --img 1400 --batch 16 --epochs 80 --data dataset.yaml --cfg yolov5m.yaml --weights yolov5m.pt --device 0 --name medium  --cache ram

uname -a
