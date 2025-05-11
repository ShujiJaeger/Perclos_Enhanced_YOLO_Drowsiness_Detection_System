# 安装指南

## 环境要求
- Python 3.8+
- PyQt5/PySide6
- OpenCV 4.5+
- PyTorch 1.10+
- CUDA 11.3+（推荐用于GPU加速）

## 安装步骤

### 1. 克隆项目到本地
```bash
git clone https://github.com/yourusername/Perclos-Enhanced-YOLO-Drowsiness-Detection-System.git
cd Perclos-Enhanced-YOLO-Drowsiness-Detection-System
```

### 2. 安装依赖

#### 标准安装方式
```bash
pip install -r requirements.txt
```

#### 如果遇到代理问题
在安装过程中，可能会遇到代理相关的错误，特别是在安装PySide6或PyQt5时。以下是几种解决方案：

##### 方案1：使用国内镜像源
```bash
# 安装PySide6
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple PySide6>=6.2.0

# 或者安装PyQt5
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple PyQt5>=5.15.0
```

##### 方案2：临时关闭代理
如果您使用了代理设置，可以尝试临时关闭代理后再安装：

在Windows系统中：
1. 打开系统设置 -> 网络和Internet -> 代理
2. 关闭"自动检测设置"和"使用代理服务器"
3. 重新运行安装命令
4. 安装完成后，可以恢复原来的代理设置

##### 方案3：单独安装其他依赖
如果UI依赖（PySide6或PyQt5）安装失败，可以先安装其他核心依赖：
```bash
pip install torch>=1.10.0 torchvision>=0.11.0 opencv-python>=4.5.0 numpy>=1.20.0 matplotlib>=3.4.0 pillow>=8.0.0 tqdm>=4.62.0 ultralytics>=8.0.0 onnx>=1.10.0 onnxruntime>=1.10.0
```

然后再尝试单独安装UI依赖。

### 3. 运行程序
安装完依赖后，可以运行主程序：
```bash
python main.py
```

## 注意事项

1. 本项目已适配PyQt5，如果成功安装了PySide6而非PyQt5，需要修改代码中的导入语句，将：
```python
from PyQt5.QtWidgets import ...
from PyQt5.QtCore import ...
from PyQt5.QtGui import ...
```
改回为：
```python
from PySide6.QtWidgets import ...
from PySide6.QtCore import ...
from PySide6.QtGui import ...
```

2. 如果使用PyQt5，需要注意Signal和Slot的导入方式与PySide6不同：
   - PySide6中直接导入Signal和Slot
   - PyQt5中需要导入pyqtSignal作为Signal，pyqtSlot作为Slot

3. 如果在运行时遇到图表相关的错误，可能需要额外安装PyQt5的图表模块：
```bash
pip install PyQt5-Charts
```

## 故障排除

如果在安装或运行过程中遇到问题，请尝试以下步骤：

1. 确保Python版本兼容（推荐Python 3.8-3.10）
2. 检查pip是否为最新版本：`pip install --upgrade pip`
3. 如果某个特定包安装失败，尝试单独安装该包
4. 对于Windows用户，某些包可能需要Visual C++ Build Tools，请确保已安装
5. 如果仍然遇到问题，请提交issue到项目仓库