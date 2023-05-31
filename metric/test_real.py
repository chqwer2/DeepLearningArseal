

from skimage.metrics import peak_signal_noise_ratio as compare_psnr
from skimage.metrics import structural_similarity as compare_ssim
import torch

def padr(img):
    pad = 20
    pad_mod = 'reflect'
    img = F.pad(input=img, pad=(pad,pad,pad,pad), mode=pad_mod)
    return img



unfold = torch.nn.Unfold(kernel_size=256, padding=2, stride=256)
(B, C, W, H) = input_noisy.shape

output = torch.zeros_like(input_noisy).to(self.device)
W_st = W// 256 + 1
H_st = H // 256 + 1
pad = 20

device = torch.device('cuda:0')

input_noisy = input_noisy.to(device)
input_GT = input_GT.to(self.device)

psnr_list =[]
ssim_list = []

# oad
for i in range(W_st):
    for j in range(H_st):
        input = padr(input_noisy[:, :, i * 256:(i + 1) * 256, j * 256:(j + 1) * 256])

        with torch.no_grad():
            clean = self.model(input)

        output[:, :, i * 256:(i + 1) * 256, j * 256:(j + 1) * 256] = \
            clean[:, :, pad:-pad, pad:-pad]

psnr = compare_psnr(output.cpu().numpy(), input_GT.cpu().numpy(), data_range=1)
ssim = compare_ssim(output.cpu().numpy(), input_GT.cpu().numpy(), data_range=1, multichannel=True, channel_axis=-1)

psnr_list.append(psnr)
ssim_list.append(ssim)

print('PSNR: ', psnr, 'SSIM: ', ssim)

print("SIDD PSNR: ", np.mean(psnr_list), ", SSIM: ", np.mean(ssim_list))



