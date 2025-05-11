# 基于Perclos与YOLOv12的疲劳驾驶检测系统

## 项目简介
本项目基于Perclos原理和YOLOv12目标检测算法，开发了一个实时疲劳驾驶检测系统。系统能够通过摄像头实时捕获驾驶员面部图像，检测眼睛开闭状态，计算PERCLOS值，并对驾驶员的疲劳状态进行判定和预警。

## 核心功能
- 人脸检测与跟踪
- 眼睛状态识别（开/闭）
- PERCLOS值实时计算
- 疲劳状态判定与预警
- 支持实时摄像头输入和视频文件处理

## 技术特点
- 采用YOLOv12最新目标检测算法，提高检测精度和速度
- 基于Qt框架开发，实现跨平台兼容性
- 优化的PERCLOS算法，提高疲劳判定准确率
- 友好的用户界面，便于操作和监控

## 系统架构
- 检测模块：负责人脸和眼睛的检测与跟踪
- 分析模块：计算PERCLOS值，判定疲劳状态
- 界面模块：提供用户交互界面，显示检测结果和预警信息

## 环境要求
- Python 3.8+
- PyQt5/PySide6
- OpenCV 4.5+
- PyTorch 1.10+
- CUDA 11.3+（推荐用于GPU加速）

## 安装与使用
1. 克隆项目到本地
```bash
git clone https://github.com/ShujiJaeger/Perclos-Enhanced-YOLO-Drowsiness-Detection-System.git
cd Perclos-Enhanced-YOLO-Drowsiness-Detection-System
```

2. 安装依赖
```bash
pip install -r requirements.txt
```

如果安装依赖时遇到问题（特别是代理相关问题），请参考 [安装指南](./INSTALL_GUIDE.md) 获取详细解决方案。

3. 运行程序
```bash
python main.py
```

## 使用说明
1. 启动程序后，选择输入源（摄像头或视频文件）
2. 调整检测参数（如需要）
3. 点击"开始检测"按钮开始疲劳驾驶检测
4. 系统将实时显示检测结果和PERCLOS值
5. 当检测到疲劳状态时，系统将发出预警

## PERCLOS原理
PERCLOS（Percentage of Eyelid Closure Over the Pupil Over Time）是指在单位时间内眼睛闭合状态所占用的时间百分比。本系统采用P80标准，即在测试过程中，眼睛闭合面积超过80%所占用的时间百分比。当PERCLOS值超过一定阈值时，判定为疲劳状态。

## 许可证
MIT License