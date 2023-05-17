### Submit Jobs

ref to https://docs.baskerville.ac.uk/jobs/#multi-gpu-multi-task-or-multi-node-jobs

```
sbatch   myscript.sh     # Return a job ID
```

Cancel Jobs

```
scancel 55260            # Calcel using job ID
```

Monitor Jobs

```
squeue -j 55620
scontrol show job 55620
```

### Job Example

See Information

```
my_baskerville
# Baskerville information for 'hxc093'
        Projects: jiaoj-3d-vision
        Default Project: jiaoj-3d-vision
        QoS: bham

An example of this is:
#SBATCH --account=jiaoj-3d-vision 
--qos=bham
```

Examples:

```
#SBATCH --account=jiaoj-3d-vision 
#SBATCH --qos=bham


---- baskstatus : Requesting GPUs
GPU Type

#SBATCH --constraint=a100_40       % a100_40 or a100_80



```

```
#!/bin/bash

module purge
module load baskerville
module load fosscuda/2020b
g++ -o gpus -lmpi -lcuda -lcudart gpus_for_tasks.cpp
srun env|grep CUDA_VISIBLE_DEVICES
srun ./gpus
```

```
#SBATCH --gpus-per-task 1
#SBATCH --tasks-per-node 2
#SBATCH --nodes 1
```





