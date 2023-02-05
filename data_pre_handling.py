"""
This helper script can generate noisy input data set
"""

import os
import cv2
import numpy as np
import random


def sp_noise(noise_img, proportion):
    """
    添加椒盐噪声
    proportion的值表示加入噪声的量，可根据需要自行调整
    return: img_noise
    """
    height, width = noise_img.shape[0], noise_img.shape[1]  # 获取高度宽度像素值
    num = int(height * width * proportion)  # 一个准备加入多少噪声小点
    for i in range(num):
        w = random.randint(0, width - 1)
        h = random.randint(0, height - 1)
        if random.randint(0, 1) == 0:
            noise_img[h, w] = 0
        else:
            noise_img[h, w] = 255
    return noise_img


def gaussian_noise(img, mean, sigma):
    """
    此函数用将产生的高斯噪声加到图片上
    传入:
        img   :  原图
        mean  :  均值
        sigma :  标准差
    返回:
        gaussian_out : 噪声处理后的图片
    """
    # 将图片灰度标准化
    img = img / 255
    # 产生高斯 noise
    noise = np.random.normal(mean, sigma, img.shape)
    # 将噪声和图片叠加
    gaussian_out = img + noise
    # 将超过 1 的置 1，低于 0 的置 0
    gaussian_out = np.clip(gaussian_out, 0, 1)
    # 将图片灰度范围的恢复为 0-255
    gaussian_out = np.uint8(gaussian_out * 255)
    # 将噪声范围搞为 0-255
    # noise = np.uint8(noise*255)
    return gaussian_out  # 这里也会返回噪声，注意返回值


def random_noise(image, noise_num):
    '''
    添加随机噪点（实际上就是随机在图像上将像素点的灰度值变为255即白色）
    param image: 需要加噪的图片
    param noise_num: 添加的噪音点数目
    return: img_noise
    '''
    # 参数image：，noise_num：
    img_noise = image
    # cv2.imshow("src", img)
    rows, cols, chn = img_noise.shape
    # 加噪声
    for i in range(noise_num):
        x = np.random.randint(0, rows)  # 随机生成指定范围的整数
        y = np.random.randint(0, cols)
        img_noise[x, y, :] = 255
    return img_noise


def convert(input_dir, output_dir, convert_type=0):
    """
    Recursively convert images into specific noisy ones.
    :param input_dir: root input dir for images
    :param output_dir: root target dir for output images
    :param convert_type: convert type
    """
    print('converting files from:' + input_dir + ' to ' + output_dir)
    assert os.path.exists(input_dir)
    if not os.path.isdir(output_dir):
        os.makedirs(output_dir)

    item_list = os.listdir(input_dir)
    if len(item_list) == 0:
        print('Input dir is empty.')
        return 0

    for item in item_list:
        next_path = os.path.join(input_dir, item)
        if os.path.isfile(next_path):
            noise_img = cv2.imread(next_path)  # 读取图片
            if convert_type == 2:
                img_noise = random_noise(noise_img, 500)  # 随机噪声
            elif convert_type == 1:
                img_noise = sp_noise(noise_img, 0.025)  # 椒盐噪声
            else:
                img_noise = gaussian_noise(noise_img, 0, 0.12)  # 高斯噪声
            target_dir = os.path.join(output_dir, item)
            # print("dump res into: ", target_dir)
            cv2.imwrite(target_dir, img_noise)
        else:
            dir_name = os.path.join(output_dir, item)
            # if dir does not exist, create one
            if not os.path.isdir(dir_name):
                os.makedirs(dir_name)
            convert(next_path, dir_name, convert_type)


if __name__ == '__main__':
    input_dir = "E:/projects/essay/data"  # 输入数据文件夹

    output_dir = "E:/projects/essay/gaussian_noise_data"  # 高斯噪声输出数据文件夹
    convert(input_dir, output_dir, convert_type=0)

    output_dir = "E:/projects/essay/salt_pepper_noise_data"  # 椒盐噪声输出数据文件夹
    convert(input_dir, output_dir, convert_type=1)

    output_dir = "E:/projects/essay/random_noise_data"  # 随机噪声输出数据文件夹
    convert(input_dir, output_dir, convert_type=2)
