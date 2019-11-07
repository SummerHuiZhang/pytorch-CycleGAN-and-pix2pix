import os
import glob
import cv2

image_path='/home/timing/Git_Repos_Summer/pytorch-CycleGAN-and-pix2pix/results/summer2winter_yosemite_pretrained/test_latest/images'
paths=glob.glob(os.path.join(image_path,'*.png'))
paths.sort()
for path in paths:
    if 'fake' in path:
        img1=cv2.imread(path)
        cv2.imshow('img_fake',img1)
        cv2.waitKey(10)
    if 'real' in path:
        img2=cv2.imread(path)
        cv2.imshow('img_real',img2)
        cv2.waitKey(1000)
#    cv2.destroyAllWindows()
