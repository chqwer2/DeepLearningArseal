
import wandb
wandb.login(key="ee52f649687b804de41f2c26b2049c7cd3e4db99")



model_name = "_bs_{}_wd_{}".format(args.batch_size, args.weight_decay)

run = wandb.init(
    # Set the project where this run will be logged
    project=project,
    # group="",
    tags="DEBUG",
    name=model_name,
    # Track hyperparameters and run metadata
    config={
        "dataset": args.dataset,
        "use_front": args.use_front,
        "use_clip": args.use_clip,
        "use_audio": args.use_audio,
        "use_360": args.use_360,
        "use_audio_tracking": args.use_audio_tracking,

        "use_video_frames": args.use_video_frames,
        "optimizer": args.optimizer,
        "fusion_method": args.fusion_method,

        "lr": args.learning_rate,
        "bs": args.batch_size}
)




# Put the log



wandb.log({'Train Loss': batch_loss,
           'Val Accuracy': acc})


