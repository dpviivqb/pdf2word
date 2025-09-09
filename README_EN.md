# PDF2Word - PDF to Word Document Converter

*[中文版本 / Chinese Version](README.md)*

A Python-based PDF to Word document conversion tool built with uv virtual environment management.

## Features

- 🔄 High-quality PDF to Word document conversion
- 📝 Preserve original formatting and layout
- 🖼️ Support for images and tables conversion
- 💻 Simple command-line interface
- ⚡ Fast processing of multi-page documents
- 🚀 **Batch conversion support** - Process multiple PDF files at once
- 🧵 **Multi-threading processing** - Accelerate batch conversions
- 📁 **Pre-configured folders** - Simple file management

## Requirements

- Python 3.12+
- uv package manager

## Installation and Usage

### Quick Start (Recommended)

1. **Clone the Repository**
```bash
git clone https://github.com/dpviivqb/pdf2word.git
cd pdf2word
```

2. **Place PDF Files**
   - Put your PDF files into the `input/` folder

3. **Run Conversion**
```bash
# Batch convert all PDF files in input/ folder
uv run main.py

# Converted Word documents will be saved in output/ folder
```

### Other Usage Options

```bash
# Convert specified single file (files not in input folder)
uv run main.py your_file.pdf

# Convert single file with specified output location
uv run main.py your_file.pdf -o output_filename.docx

# Use 8 threads for faster batch conversion (for files in input/ folder)
uv run main.py --threads 8

# View help information
uv run main.py --help
```

### Traditional Method (Optional, for users without uv)

```bash
# Create virtual environment
python -m venv .venv

# Activate virtual environment
source .venv/bin/activate

# Install dependencies
pip install pdf2docx python-docx PyPDF2

# Run the program
python main.py
```

## Tech Stack

- **pdf2docx**: Core PDF conversion library
- **python-docx**: Word document processing
- **PyPDF2**: PDF file operations
- **argparse**: Command-line argument parsing

## Project Structure

```text
pdf2word/
├── input/              # 📁 Place PDF files here for conversion
├── output/             # 📄 Converted Word documents
├── .venv/              # Virtual environment
├── main.py             # Main program
├── pyproject.toml      # Project configuration
├── LICENSE             # License file
├── README.md           # Documentation (Chinese)
├── README_EN.md        # Documentation (English)
└── .gitignore          # Git ignore rules
```

## Conversion Quality

This tool uses the pdf2docx library, which can:

- Preserve text formatting and font styles
- Convert table structures
- Retain images and charts
- Maintain page layout

## Troubleshooting

If you encounter conversion issues, please check:

1. Whether the PDF file is corrupted
2. Whether there is sufficient disk space
3. Whether the virtual environment is properly activated

## Contributing

Feel free to submit issues and enhancement requests!

## License

MIT License

---

*[中文版本 / Chinese Version](README.md)*
