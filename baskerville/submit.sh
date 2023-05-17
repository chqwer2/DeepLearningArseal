#!/bin/bash.sh

#SBATCH --account=jiaoj-3d-vision
#SBATCH --qos=bham
#SBATCH --time 0:10:0
#SBATCH --nodes 1
#SBATCH --gpus 0
#SBATCH --cpus-per-gpu 36
#SBATCH --job-name <job_name>

module purge; module load baskerville
module load bask-apps/live
module load fosscuda/2020b

#./cudaOpenMP