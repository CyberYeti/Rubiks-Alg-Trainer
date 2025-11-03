from ultralytics import YOLO
from time import sleep

model= YOLO('yolov8s-obb.pt')  # load a pretrained model (recommended for training)
results = model.track("https://ultralytics.com/images/boats.jpg", show=True, save=True)  # predict on an image

sleep(200)  # wait for 2 seconds to view the image