import os
import re
import json
import time
import cv2
import numpy as np
from icecream import ic
from skimage.color import rgb2lab, lab2rgb
from collections import Counter
from moviepy.editor import VideoFileClip

from model import Seg


BASE_PATH = '../../video'
ELAPSE_DICT = dict()
SEGS_LIST = list()


def get_image_eigenvalue(image, n_colors=5):
    avg_pre_row = image.mean(axis=0)
    avg = avg_pre_row.mean(axis=0)
    return avg
    image_lab = rgb2lab(image)
    # print(image)
    color_list = image_lab.reshape((image_lab.shape[0]*image_lab.shape[1], 3))
    common_colors = Counter([tuple(colors) for colors in color_list]).most_common(n_colors)
    return common_colors[0][0]
    

def get_eigenvalue(seg_path):
    clip = VideoFileClip(seg_path)
    frame_rate = clip.fps
    frame_num = int(clip.duration * clip.fps)
    total_time = int(frame_num / frame_rate)
    colors = np.array((0, 0, 0))
    # ic(frame_rate)
    # ic(frame_num)
    for i in range(0, total_time):
        # ic(i)
        # ic(frame)
        # ic(frame.shape)
        frame = clip.get_frame(i)
        image_eigenvalue = get_image_eigenvalue(frame)
        colors = colors + (image_eigenvalue)
    eigenvalue = np.int64(colors / int(total_time))
    # eigenvalue = Counter([tuple(color) for color in colors]).most_common(1)[0][0]
    return eigenvalue.tolist()


def get_duration(seg_path):
    clip = VideoFileClip(seg_path)
    return clip.duration

def get_size(seg_path):
    clip = VideoFileClip(seg_path)
    return clip.size

def entry(movie_title='Pulp Fiction'):
    movie_title = str(movie_title).replace(' ', '-').lower()
    video_path = os.path.join(BASE_PATH, movie_title)
    total = 0
    for root, dirs, files in os.walk(video_path, topdown=False):
        for file in files:
            seg = Seg()
            seg_path = os.path.join(root, file)
            seg_id = re.findall(r'\d+', str(file))[0]
            seg_elapse = get_duration(seg_path)
            seg_size = get_size(seg_path)
            seg_eigenvalue = get_eigenvalue(seg_path)
            ELAPSE_DICT[seg_id] = seg_elapse
            (seg.id, seg.size, seg.elapse, seg.eigenvalue) = (seg_id, seg_size, seg_elapse, seg_eigenvalue)
            SEGS_LIST.append(seg)
            total = total + 1
            print(total, end='\r')
            # if total == 10:
            #     break
    # print(SEGS_LIST)
    SEGS_LIST.sort(key=lambda x: x.id)
    cnt = 0
    for seg in SEGS_LIST:
        seg.start = cnt
        seg.end = seg.start + seg.elapse
        cnt = seg.end
    return [seg.to_json() for seg in SEGS_LIST]



if __name__ == '__main__':
    movie_title = input('enter movie title: ')
    entry()

    # print(get_eigenvalue('/home/blank/repo_pro/project-spectrums/spectrums/video/pulp-fiction/pulp-fiction-0020.mp4'))
