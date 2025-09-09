import os
import sys
from pathlib import Path
from pdf2docx import Converter
import argparse


def pdf_to_word(pdf_path: str, output_path: str = None) -> str:
    """
    Convert PDF file to Word document
    
    Args:
        pdf_path (str): Path to the input PDF file
        output_path (str): Path for the output Word file (optional)
    
    Returns:
        str: Path to the converted Word file
    """
    # Validate input file
    if not os.path.exists(pdf_path):
        raise FileNotFoundError(f"PDF file not found: {pdf_path}")
    
    if not pdf_path.lower().endswith('.pdf'):
        raise ValueError("Input file must be a PDF file")
    
    # Generate output path if not provided
    if output_path is None:
        pdf_file = Path(pdf_path)
        output_path = pdf_file.with_suffix('.docx')
    
    # Ensure output directory exists
    output_dir = Path(output_path).parent
    output_dir.mkdir(parents=True, exist_ok=True)
    
    try:
        # Convert PDF to Word
        print(f"Converting {pdf_path} to {output_path}...")
        cv = Converter(pdf_path)
        cv.convert(output_path, start=0, end=None)
        cv.close()
        print(f"✅ Conversion completed successfully!")
        print(f"📄 Output file: {output_path}")
        return str(output_path)
        
    except Exception as e:
        print(f"❌ Error during conversion: {str(e)}")
        raise


def main():
    """Main function with command line interface"""
    parser = argparse.ArgumentParser(description='Convert PDF to Word document')
    parser.add_argument('pdf_file', help='Path to the PDF file to convert')
    parser.add_argument('-o', '--output', help='Output Word file path (optional)')
    parser.add_argument('--version', action='version', version='PDF2Word 1.0.0')
    
    args = parser.parse_args()
    
    try:
        output_file = pdf_to_word(args.pdf_file, args.output)
        return 0
    except Exception as e:
        print(f"Error: {str(e)}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
