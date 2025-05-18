"""
基于Perclos与YOLOv12的疲劳驾驶检测系统
主程序入口
"""
import sys
import os
import cv2
import numpy as np
from PyQt5.QtWidgets import QApplication
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from ui.main_window import MainWindow
from models.yolov12_model import YOLOv12Model
from utils.perclos import PerclosCalculator
from utils.face_detector import FaceDetector
from utils.eye_tracker import EyeTracker

def main():
    """主函数"""
    app = QApplication(sys.argv)
    app.setApplicationName('疲劳驾驶检测系统')
    model_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
        'models', 'weights', 'yolov12n.pt')
    if not os.path.exists(model_path):
        print(f'警告: 模型文件 {model_path} 不存在，请先下载模型权重文件')
        os.makedirs(os.path.dirname(model_path), exist_ok=True)
    yolo_model = YOLOv12Model(model_path)
    face_detector = FaceDetector(yolo_model)
    eye_tracker = EyeTracker()
    perclos_calculator = PerclosCalculator()
    main_window = MainWindow(yolo_model, face_detector, eye_tracker,
        perclos_calculator)
    main_window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
