import math
from math import log10, sqrt
import os
import cv2
from skimage.metrics import structural_similarity
import imutils
import numpy as np

def PSNR(begin, sr):
    original = cv2.imread(begin)
    compressed = cv2.imread(sr)
    mse = np.mean((original - compressed) ** 2)
    if (mse == 0):  # MSE is zero means no noise is present in the signal .
        # Therefore PSNR have no importance.
        return 100
    max_pixel = 255.0
    psnr = 20 * log10(max_pixel / sqrt(mse))
    return psnr


def SSIM(begin, sr):
    original = cv2.imread(begin)
    compressed = cv2.imread(sr)
    #print(begin)
    #print(sr)
    grayA = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)
    grayB = cv2.cvtColor(compressed, cv2.COLOR_BGR2GRAY)

    (ssim, diff) = structural_similarity(grayA, grayB, full=True)
    diff = (diff * 255).astype("uint8")

    # print("SSIM: {}".format(ssim))
    return ssim

def psnr_for_files(original_dir, completed_dir):
    original_files = os.listdir(original_dir)
    completed_files = os.listdir(completed_dir)
    psnrs = []
    for file in original_files:
        name = os.path.splitext(file)[0]
        psnr = PSNR(original_dir + "/" + file, completed_dir + "/" + name + '.png')
        psnrs.append(psnr)

    return psnrs


def ssim_for_files(original_dir, completed_dir):
    original_files = os.listdir(original_dir)
    completed_files = os.listdir(completed_dir)
    ssims = []
    for file in original_files:
        name = os.path.splitext(file)[0]
        ssim = SSIM(original_dir + "/" + file, completed_dir + "/" + name + '.png')
        ssims.append(ssim)

    return ssims

def variance(data, ddof=0):
    n = len(data)
    mean = sum(data) / n
    return sum((x - mean) ** 2 for x in data) / (n - ddof)


def stdev(data):
    var = variance(data)
    std_dev = math.sqrt(var)
    return std_dev


def main():
    psnr = psnr_for_files("IMAGES/ORIG", "IMAGES/SR")
    ssim = ssim_for_files("IMAGES/ORIG", "IMAGES/SR")

    print(psnr)
    print(ssim)

    print("psnr")
    print(variance(psnr))
    print(stdev(psnr))
    print(max(psnr))
    print(min(psnr))
    print(sum(psnr)/len(psnr))


    print("ssim")
    print(variance(ssim))
    print(stdev(ssim))
    print(max(ssim))
    print(min(ssim))
    print(sum(ssim)/len(ssim))




if __name__ == "__main__":
    main()

