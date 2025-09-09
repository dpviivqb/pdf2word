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
- 📁 **Flexible file handling** - Support for relative and absolute paths
- 🕒 **Smart duplicate handling** - Auto timestamp to avoid file overwriting
- 📂 **Multiple input methods** - Support for single files, directories, and wildcard patterns

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
uv run -m pdf2word

# Converted Word documents will be saved in output/ folder
```

### Other Usage Options

```bash
# Convert specified single file (files not in input folder)
uv run -m pdf2word your_file.pdf

# Convert specified single file (absolute path)
uv run -m pdf2word "/Users/username/Documents/document.pdf"

# Convert single file with specified output location
uv run -m pdf2word your_file.pdf -o output_filename.docx

# Convert file to specified absolute path
uv run -m pdf2word document.pdf -o "/Users/username/Desktop/converted.docx"

# Use 8 threads for faster batch conversion (for files in input/ folder)
uv run -m pdf2word --threads 8

# View help information
uv run -m pdf2word --help
```

### Practical Usage Examples

```bash
# Example 1: Batch convert all PDFs in current directory
uv run -m pdf2word .

# Example 2: Convert PDFs from specified directory
uv run -m pdf2word "/path/to/pdf/folder" -o "/path/to/output/folder"
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
python -m pdf2word
```

## Tech Stack

- **pdf2docx**: Core PDF conversion library
- **python-docx**: Word document processing
- **PyPDF2**: PDF file operations
- **argparse**: Command-line argument parsing

## Project Structure

```text
pdf2word/
├── src/
│   └── pdf2word/           # 📦 Core code package
│       ├── __init__.py     # Package initialization
│       ├── __main__.py     # Module entry point
│       ├── main.py         # Main program logic
│       ├── converter.py    # PDF conversion core functionality
│       └── utils.py        # Utility functions
├── input/                  # 📁 Place PDF files here for conversion
├── output/                 # 📄 Converted Word documents
├── .venv/                  # Virtual environment
├── pyproject.toml          # Project configuration
├── LICENSE                 # License file
├── README.md               # Documentation (Chinese)
├── README_EN.md            # Documentation (English)
└── .gitignore              # Git ignore rules
```

## Conversion Quality

This tool uses the pdf2docx library, which can:

- Preserve text formatting and font styles
- Convert table structures
- Retain images and charts
- Maintain page layout

## Smart Duplicate Handling

When an output file already exists, the program automatically adds a timestamp to avoid overwriting:

- **Timestamp Format**: `YYYYMMDD_HHMMSS`
- **Example**: `document.docx` → `document_20250909_154908.docx`
- **Use Cases**:
  - Multiple conversions of the same PDF file
  - Avoiding overwrite during batch processing
  - Preserving conversion history

```bash
# Example: Multiple conversions generate files with different timestamps
output/
├── Survey.docx                    # First conversion
├── Survey_20250909_154836.docx   # Second conversion
└── Survey_20250909_154908.docx   # Third conversion
```

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
