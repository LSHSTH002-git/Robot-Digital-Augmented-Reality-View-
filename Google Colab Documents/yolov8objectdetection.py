# -*- coding: utf-8 -*-
"""YOLOv8ObjectDetection.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1LauoXOv-gq_PdrztojaDKPGMazR1qS42

Installing YOLOv8
"""

!nvidia-smi

!pip install ultralytics;

from ultralytics import YOLO
import os
from IPython.display import display, Image
from IPython import display
display.clear_output();

"""Training YOLOv8 On Data collected from Image processing Lab"""

!pip install roboflow

from roboflow import Roboflow
rf = Roboflow(api_key="pu your own, cannot compromise mine")
project = rf.workspace("eee4022f").project("objectdetection4022f")
version = project.version(1)
dataset = version.download("yolov8")

!yolo task=detect mode=train model=yolov8m.pt data={dataset.location} epochs=30 imgsz=640
