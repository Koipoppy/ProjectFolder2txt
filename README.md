# ProjectFolder2txt

一个功能强大的项目文件合并工具，可以将整个项目的代码文件合并生成一个总览文档，支持GUI界面操作和实时进度显示。

## 🌟 功能特性

- ✅ **图形化界面**：基于PyQt5的友好用户界面
- ✅ **拖拽支持**：支持拖拽项目目录到界面
- ✅ **智能过滤**：自动排除版本控制、缓存等非代码文件
- ✅ **进度显示**：实时显示处理进度和详细日志
- ✅ **多格式支持**：支持30+种代码文件格式
- ✅ **编码兼容**：自动处理不同编码格式的文件
- ✅ **目录结构**：生成清晰的项目目录树状图
- ✅ **一键操作**：简单易用的文件选择和输出功能

## 📁 支持的文件类型

### 编程语言
- **Python** (`.py`)
- **Java** (`.java`)
- **C/C++** (`.c`, `.cpp`, `.h`, `.hpp`)
- **JavaScript/TypeScript** (`.js`, `.ts`)
- **Go** (`.go`)
- **Rust** (`.rs`)
- **PHP** (`.php`)
- **Ruby** (`.rb`)

### 标记和配置
- **HTML/CSS** (`.html`, `.css`)
- **JSON/YAML** (`.json`, `.yaml`, `.yml`)
- **XML** (`.xml`)
- **Markdown** (`.md`)
- **Text** (`.txt`)
- **Configuration** (`.ini`, `.conf`)

### 脚本和数据库
- **Shell** (`.sh`, `.bash`)
- **SQL** (`.sql`)

## 🚀 快速开始

### 环境要求

- Python 3.6+
- PyQt5
- PyInstaller (可选，用于打包)

### 安装依赖

```bash
pip install -r requirements.txt
```

### 运行程序

```bash
python main.py
```

### 打包可执行文件

```bash
cd utils
pyinstaller project_combiner.spec
```

## 📖 使用方法

1. **启动程序**：运行 `main.py` 或编译后的可执行文件
2. **选择项目**：点击"浏览..."按钮或拖拽项目目录到界面
3. **设置输出**：选择输出文件路径（默认为 `project_combined.txt`）
4. **开始生成**：点击"开始生成"按钮
5. **查看结果**：生成完成后可打开或复制输出文件

## 📊 项目结构

```
项目总览生成工具/
├── src/                          # 源代码目录
│   └── project_combiner.py       # 主要功能实现
├── utils/                        # 工具文件
│   └── project_combiner.spec     # PyInstaller配置文件
├── tests/                        # 测试文件
│   └── test_project_combiner.py  # 单元测试
├── docs/                         # 文档
│   └── usage.md                  # 使用说明
├── examples/                     # 示例项目
│   └── example_project/          # 示例项目目录
├── requirements.txt              # 项目依赖
├── main.py                       # 程序入口
└── README.md                     # 项目说明
```

## 🔧 技术栈

- **开发语言**：Python 3.x
- **GUI框架**：PyQt5
- **打包工具**：PyInstaller
- **测试框架**：unittest

## 📝 项目命名

本项目命名为 **ProjectFolder2txt**，寓意将项目文件夹（ProjectFolder）转换为文本（txt）文件，简洁明了地表达了工具的核心功能。

## 🎯 使用场景

- **代码审查**：快速生成项目代码总览
- **文档生成**：创建项目代码文档
- **备份归档**：将项目代码整合保存
- **学习分析**：分析开源项目结构
- **代码分享**：生成便于分享的代码文档

## 🔍 输出格式

生成的文档包含：

1. **项目目录结构**：树状图显示项目文件结构
2. **代码文件内容**：按顺序显示所有代码文件内容
3. **文件信息**：包含文件路径、编号等信息

## ⚙️ 配置选项

### 排除目录
工具会自动排除以下目录：
- `.git` - Git版本控制
- `__pycache__` - Python缓存
- `venv`, `env` - 虚拟环境
- `node_modules` - Node.js依赖
- `.idea` - IntelliJ项目配置
- `.vscode` - VS Code配置

### 文件编码
支持多种文件编码：
- UTF-8
- Latin-1
- UTF-16

## 🐛 问题反馈

如遇到问题，请检查：
1. Python环境是否正确配置
2. PyQt5是否正确安装
3. 项目路径是否有读取权限
4. 输出目录是否有写入权限

## 📄 许可证

MIT License - 详见LICENSE文件

## 🙋‍♂️ 贡献

欢迎提交Issue和Pull Request来改进这个项目！

## 📞 联系方式

如有问题或建议，请通过以下方式联系：
- 提交GitHub Issue
- 发送邮件到：[chenyuchong2005@163.com](mailto:chenyuchong2005@163.com)

---

**⭐ 如果这个项目对你有帮助，请给个Star支持一下！**