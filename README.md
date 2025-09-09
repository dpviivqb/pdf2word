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
- 🕒 **智能重名处理** - 自动添加时间戳避免覆盖文件

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
uv run -m pdf2word

# 转换完成的Word文档将保存在 output/ 文件夹中
```

### 其他使用方式

```bash
# 转换指定的单个文件（不在input文件夹中的文件）
uv run -m pdf2word your_file.pdf

# 转换单个文件并指定输出位置
uv run -m pdf2word your_file.pdf -o output_filename.docx

# 使用8个线程加速批量转换（处理input/文件夹中的文件）
uv run -m pdf2word --threads 8

# 查看帮助信息
uv run -m pdf2word --help
```

### 传统方式（可选，适用于没有uv的用户）

```bash
# 创建虚拟环境
python -m venv .venv

# 激活虚拟环境
source .venv/bin/activate

# 安装依赖
pip install pdf2docx python-docx PyPDF2

# 运行程序
python -m pdf2word
```

## 技术栈

- **pdf2docx**: 核心PDF转换库
- **python-docx**: Word文档处理
- **PyPDF2**: PDF文件操作
- **argparse**: 命令行参数解析

## 项目结构

```text
pdf2word/
├── src/
│   └── pdf2word/           # 📦 核心代码包
│       ├── __init__.py     # 包初始化文件
│       ├── __main__.py     # 模块入口点
│       ├── main.py         # 主程序逻辑
│       ├── converter.py    # PDF转换核心功能
│       └── utils.py        # 工具函数
├── input/                  # 📁 放入需要转换的PDF文件
├── output/                 # 📄 转换完成的Word文档
├── .venv/                  # 虚拟环境
├── pyproject.toml          # 项目配置
├── LICENSE                 # 许可证文件
├── README.md               # 说明文档（中文）
├── README_EN.md            # 说明文档（英文）
└── .gitignore              # Git 忽略规则
```

## 转换质量说明

该工具使用pdf2docx库，能够：
- 保持文本格式和字体样式
- 转换表格结构
- 保留图片和图表
- 维持页面布局

## 智能重名处理

当输出文件已存在时，程序会自动添加时间戳避免覆盖：

- **时间戳格式**：`YYYYMMDD_HHMMSS`
- **示例**：`document.docx` → `document_20250909_154908.docx`
- **适用场景**：
  - 多次转换同一PDF文件
  - 批量处理时避免覆盖已有文件
  - 保留转换历史记录

```bash
# 示例：多次转换会生成不同时间戳的文件
output/
├── Survey.docx                    # 第一次转换
├── Survey_20250909_154836.docx   # 第二次转换
└── Survey_20250909_154908.docx   # 第三次转换
```

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
