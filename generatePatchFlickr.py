import os.path
import matplotlib.pyplot as plt
import os
import random
import numpy as np
import sys
from PIL import Image
from PIL import ImageFilter


ori_data_dir = 'Flickr/train_images/'
ori_data_dir = sys.argv[1]
output_path = 'Flickr/Flick_patch/'
output_path = sys.argv[2]
imgNames = os.listdir(ori_data_dir)

patch_size = [256, 256]

sample_num_for_each_seq = 20
sample_idx = 0

for im_name in imgNames:

    seq_path = ori_data_dir + im_name

    img = Image.open(seq_path)
    im_height = img.height
    im_width = img.width

    img_arr = np.array(img)

    if len(img_arr.shape) < 3:
        continue

    sample_num_for_each_seq = int(im_height * im_width / patch_size[0] / patch_size[1]) * 4

    for sample_id in range(sample_num_for_each_seq):
        random_resize_factor = random.random() * 0.4 + 0.6  #random 0.6 - 1.0 resize
        crop_size = [round(patch_size[0] / random_resize_factor), round(patch_size[1] / random_resize_factor)]

        random_crop_x1 = 0 + int(random.random() * (im_width - crop_size[1] - 2))
        random_crop_y1 = 0 + int(random.random() * (im_height - crop_size[0] - 2))
        random_crop_x2 = random_crop_x1 + crop_size[1]
        random_crop_y2 = random_crop_y1 + crop_size[0]

        random_box = (random_crop_x1, random_crop_y1, random_crop_x2, random_crop_y2)

        sample_array = None

        randomCropPatch = img.crop(random_box)
        randomCropPatch = randomCropPatch.resize(patch_size, Image.BICUBIC)

        sample_out_path = output_path + im_name[0:len(im_name) - 4] + "_%04d.png" % (sample_id)
        randomCropPatch.save(sample_out_path)

    sample_idx += 1

    if sample_idx % 10 == 0:
        # break
        print(sample_idx)
