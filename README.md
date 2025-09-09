# PDF2Word - PDF转Word文档工具

*[English Version / 英文版本](README_EN.md)*

这是一个使用Python和uv虚拟环境开发的PDF转Word文档转换工具。

## 功能特性

- 🔄 高质量PDF到Word文档转换
- 📝 保持原始格式和布局
- 🖼️ 支持图片和表格转换
- 💻 简单的命令行界面
- ⚡ 快速处理多页文档

## 环境要求

- Python 3.12+
- uv包管理器

## 安装和使用

### 1. 克隆仓库
```bash
git clone https://github.com/dpviivqb/pdf2word.git
cd pdf2word
```

### 2. 使用 uv 运行（推荐）
```bash
# 直接使用 uv 运行，无需手动管理虚拟环境
uv run main.py your_file.pdf

# 指定输出文件名
uv run main.py your_file.pdf -o output_filename.docx

# 查看帮助信息
uv run main.py --help
```

### 3. 传统方式（可选）
```bash
# 激活虚拟环境
source .venv/bin/activate

# 安装依赖
pip install -r requirements.txt

# 运行程序
python main.py your_file.pdf
```

### 4. 示例
```bash
# 使用 uv 将 Survey.pdf 转换为 Survey.docx
uv run main.py Survey.pdf

# 转换并指定输出路径
uv run main.py Survey.pdf -o /path/to/output/document.docx

# 转换 Lecture-04.pdf
uv run main.py Lecture-04.pdf -o Lecture-04.docx
```

## 技术栈

- **pdf2docx**: 核心PDF转换库
- **python-docx**: Word文档处理
- **PyPDF2**: PDF文件操作
- **argparse**: 命令行参数解析

## 项目结构

```
pdf2word/
├── .venv/              # 虚拟环境
├── main.py             # 主程序
├── pyproject.toml      # 项目配置
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
