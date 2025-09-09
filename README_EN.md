# PDF2Word - PDF to Word Document Converter

*[中文版本 / Chinese Version](README.md)*

A Python-based PDF to Word document conversion tool built with uv virtual environment management.

## Features

- 🔄 High-quality PDF to Word document conversion
- 📝 Preserve original formatting and layout
- 🖼️ Support for images and tables conversion
- 💻 Simple command-line interface
- ⚡ Fast processing of multi-page documents

## Requirements

- Python 3.12+
- uv package manager

## Installation and Usage

### 1. Clone the Repository
```bash
git clone https://github.com/dpviivqb/pdf2word.git
cd pdf2word
```

### 2. Using uv (Recommended)
```bash
# Run directly with uv, no need to manually manage virtual environment
uv run main.py your_file.pdf

# Specify output filename
uv run main.py your_file.pdf -o output_filename.docx

# View help information
uv run main.py --help
```

### 3. Traditional Method (Optional)
```bash
# Activate virtual environment
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the program
python main.py your_file.pdf
```

### 4. Examples
```bash
# Convert Survey.pdf to Survey.docx using uv
uv run main.py Survey.pdf

# Convert with specified output path
uv run main.py Survey.pdf -o /path/to/output/document.docx

# Convert Lecture-04.pdf
uv run main.py Lecture-04.pdf -o Lecture-04.docx

# Convert SLR_v1.0.pdf
uv run main.py SLR_v1.0.pdf -o SLR_v1.0.docx
```

## Tech Stack

- **pdf2docx**: Core PDF conversion library
- **python-docx**: Word document processing
- **PyPDF2**: PDF file operations
- **argparse**: Command-line argument parsing

## Project Structure

```
pdf2word/
├── .venv/              # Virtual environment
├── main.py             # Main program
├── pyproject.toml      # Project configuration
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
