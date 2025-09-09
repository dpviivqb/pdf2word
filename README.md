# PDF2Word - PDF转Word文档工具

*[English Version / 英文版本](README_EN.md)*

这是一个使用Python和uv虚拟环境开发的PDF转Word文档转换工具。

## 功能特性

- 🔄 高质量PDF到Word文档转换
- 📝 保持原始格式和布局
- 🖼️ 支持图片和表格转换
- 💻 简单的命令行界面
- ⚡ 快速处理多页文档
- 🚀 **批量转换支持** - 一次处理多个PDF文件
- 🧵 **多线程处理** - 加速批量转换
- 📁 **预设文件夹** - 简单的文件管理

## 环境要求

- Python 3.12+
- uv包管理器

## 安装和使用

### 快速开始 (推荐)

1. **克隆仓库**
```bash
git clone https://github.com/dpviivqb/pdf2word.git
cd pdf2word
```

2. **放入PDF文件**
   - 将需要转换的PDF文件放入 `input/` 文件夹

3. **运行转换**
```bash
# 批量转换 input/ 文件夹中的所有PDF文件
uv run main.py

# 转换完成的Word文档将保存在 output/ 文件夹中
```

### 其他使用方式

```bash
# 转换单个文件
uv run main.py your_file.pdf

# 转换单个文件并指定输出位置
uv run main.py your_file.pdf -o output_filename.docx

# 使用8个线程加速批量转换
uv run main.py --threads 8

# 查看帮助信息
uv run main.py --help
```

### 传统方式（可选）

```bash
# 激活虚拟环境
source .venv/bin/activate

# 安装依赖
pip install -r requirements.txt

# 运行程序
python main.py
```

## 技术栈

- **pdf2docx**: 核心PDF转换库
- **python-docx**: Word文档处理
- **PyPDF2**: PDF文件操作
- **argparse**: 命令行参数解析

## 项目结构

```text
pdf2word/
├── input/              # 📁 放入需要转换的PDF文件
├── output/             # 📄 转换完成的Word文档
├── .venv/              # 虚拟环境
├── main.py             # 主程序
├── pyproject.toml      # 项目配置
├── LICENSE             # 许可证文件
├── README.md           # 说明文档（中文）
├── README_EN.md        # 说明文档（英文）
└── .gitignore          # Git 忽略规则
```

## 转换质量说明

该工具使用pdf2docx库，能够：
- 保持文本格式和字体样式
- 转换表格结构
- 保留图片和图表
- 维持页面布局

## 故障排除

如果遇到转换问题，请检查：
1. PDF文件是否损坏
2. 是否有足够的磁盘空间
3. 虚拟环境是否正确激活

## 贡献

欢迎随时提交issues和改进建议！

## 许可证

MIT License

---

*[English Version / 英文版本](README_EN.md)*
