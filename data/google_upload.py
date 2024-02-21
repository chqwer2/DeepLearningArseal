from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive


gauth = GoogleAuth()
drive = GoogleDrive(gauth)

file1 = drive.CreateFile({'title': 'Hello.txt'})
file1.Upload()



# "/bask/projects/j/jiaoj-3d-vision/Hao/medical/Dataset/Prostate/data/promise12_finer_img_window_lam_0.1.npy"
# "/bask/projects/j/jiaoj-3d-vision/Hao/medical/Dataset/Prostate/data/promise12_pseudo_mask.npy"
# "/bask/projects/j/jiaoj-3d-vision/Hao/medical/Test_Time_Adaptation/exp/ours/result/benchmark_resnet34_fold0_epoch6_dice=0.6376389861106873.pth"

