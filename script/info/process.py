import os
import re
import json
import time
import cv2
from moviepy.editor import VideoFileClip

from model import Seg

BASE_PATH = '../../video'
ELAPSE_DICT = dict()
SEGS_LIST = list()

def extract(seg_path):
    pass

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
            ELAPSE_DICT[seg_id] = seg_elapse
            (seg.id, seg.size, seg.elapse) = (seg_id, seg_size, seg_elapse)
            SEGS_LIST.append(seg)
            total = total + 1
            print(total, end='\r')
    print(SEGS_LIST)

            




if __name__ == '__main__':
    movie_title = input('enter movie title: ')
    entry()
