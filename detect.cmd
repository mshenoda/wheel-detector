python .\yolov5\detect.py --source %1 --name %2  --weights .\wheel_detector.pt --conf-thres 0.3 --iou-thres 0.4 --save-txt --hide-label 

@echo off
IF exist output ( echo output dircty exists ) ELSE ( mkdir output && echo output directory created)

move .\yolov5\runs\detect\%2 .\output\
