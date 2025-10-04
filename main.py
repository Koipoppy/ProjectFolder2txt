#!/usr/bin/env python3
"""
ProjectFolder2txt - 主入口文件

这是一个用于将项目文件合并生成总览文档的工具，支持拖拽操作和进度显示。
"""

import sys
import os

# 将src目录添加到Python路径
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from project_combiner import ProjectCombinerUI
from PyQt5.QtWidgets import QApplication

def main():
    """主函数"""
    app = QApplication(sys.argv)
    app.setApplicationName("ProjectFolder2txt")
    app.setApplicationVersion("1.0.0")
    
    window = ProjectCombinerUI()
    window.show()
    
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()