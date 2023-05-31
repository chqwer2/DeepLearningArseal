from torch.utils.data import Dataset

from glob import glob
from PIL import Image
import random
import numpy as np


class PolyU(Dataset):
    def __init__(self,  **kwargs):
        super().__init__( **kwargs)

        self.paths_L = glob("../../../../../data/denoising/PolyU/noisy/*")
        self.paths_H = glob("../../../../../data/denoising/PolyU/gt/*")
        self.paths_H.sort()
        self.paths_L.sort()

        # *255

    def __len__(self):
        return len(self.paths_H)

    def get_img_by_index(self, index):
        H_path = self.paths_H[index]
        L_path = self.paths_L[index]#.replace("/gt", "/noisy")

        # print("L_path:", L_path)

        img_H = Image.open(H_path)
        img_L = Image.open(L_path)

        img_H = np.asarray(img_H).transpose(2, 0, 1)
        img_L = np.asarray(img_L).transpose(2, 0, 1)

        # (npImg_noisy, (2, 0, 1)) / 255)

        # print("img_L max:", np.max(img_L)) # 255

        if np.max(img_H) > 1.1:
            img_H = img_H / 255
            img_L = img_L / 255

        return img_H, img_L


    def __getitem__(self, idx):
        '''
        final dictionary shape of data:
        {'clean', 'syn_noisy', 'real_noisy', 'noisy (any of real[first priority] and syn)', etc}
        '''
        # calculate data index
        data_idx = idx #% self.n_data

        # load data
        img_H, img_L = self.get_img_by_index(data_idx)


        return np.array(img_H, dtype=np.float32),  np.array(img_L, dtype=np.float32)


from torch.utils.data import DataLoader
# train_dataloader = DataLoader(train_dataset, batch_size=args.batch_size,
#                               shuffle=True, num_workers=8, pin_memory=True)   #non_blocking=True
#
test_dataloader = DataLoader(test_dataset, batch_size=1,
                             shuffle=False, num_workers=8, pin_memory=True)  #
