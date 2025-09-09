"""
OCR enhancement proposal for PDF2Word converter
"""

import os
from pathlib import Path
from typing import List, Tuple
import tempfile

# Proposed new dependencies for OCR support
# pip install pytesseract pdf2image pillow

try:
    import pytesseract
    from pdf2image import convert_from_path
    from PIL import Image
    OCR_AVAILABLE = True
except ImportError:
    OCR_AVAILABLE = False


def detect_pdf_type(pdf_path: str) -> str:
    """
    Detect if PDF contains selectable text or is image-based
    
    Args:
        pdf_path (str): Path to PDF file
        
    Returns:
        str: 'text', 'image', or 'mixed'
    """
    try:
        from PyPDF2 import PdfReader
        
        reader = PdfReader(pdf_path)
        text_content = ""
        
        # Check first few pages for text content
        max_pages = min(3, len(reader.pages))
        for i in range(max_pages):
            text_content += reader.pages[i].extract_text()
        
        # Determine PDF type based on text content
        if len(text_content.strip()) > 100:
            return 'text'
        elif len(text_content.strip()) == 0:
            return 'image'
        else:
            return 'mixed'
            
    except Exception:
        return 'unknown'


def ocr_pdf_to_text(pdf_path: str, language: str = 'eng+chi_sim') -> List[str]:
    """
    Convert PDF to text using OCR
    
    Args:
        pdf_path (str): Path to PDF file
        language (str): Tesseract language code
        
    Returns:
        List[str]: List of text content for each page
    """
    if not OCR_AVAILABLE:
        raise ImportError("OCR dependencies not installed. Run: pip install pytesseract pdf2image")
    
    # Convert PDF pages to images
    with tempfile.TemporaryDirectory() as temp_dir:
        images = convert_from_path(pdf_path, dpi=300)
        
        page_texts = []
        for i, image in enumerate(images):
            print(f"🔍 OCR processing page {i+1}/{len(images)}...")
            
            # Perform OCR on image
            text = pytesseract.image_to_string(image, lang=language)
            page_texts.append(text)
        
        return page_texts


def enhanced_pdf_to_word(pdf_path: str, output_path: str = None, use_ocr: bool = False, ocr_fallback: bool = True) -> str:
    """
    Enhanced PDF to Word conversion with OCR support
    
    Args:
        pdf_path (str): Path to PDF file
        output_path (str): Output Word file path
        use_ocr (bool): Force use OCR even for text PDFs
        ocr_fallback (bool): Use OCR as fallback for image PDFs
        
    Returns:
        str: Path to converted Word file
    """
    pdf_type = detect_pdf_type(pdf_path)
    print(f"📋 PDF type detected: {pdf_type}")
    
    if use_ocr or (ocr_fallback and pdf_type in ['image', 'mixed']):
        if not OCR_AVAILABLE:
            print("⚠️ OCR not available, falling back to standard conversion")
            return standard_pdf_to_word(pdf_path, output_path)
        
        print("🔍 Using OCR for text extraction...")
        # OCR processing logic here
        # This would require additional implementation to convert OCR text to Word
        
        # For now, fall back to standard conversion
        return standard_pdf_to_word(pdf_path, output_path)
    else:
        print("📝 Using standard text extraction...")
        return standard_pdf_to_word(pdf_path, output_path)


def standard_pdf_to_word(pdf_path: str, output_path: str = None) -> str:
    """
    Standard PDF to Word conversion (current implementation)
    """
    # This would be your existing pdf_to_word function
    pass


# Example usage in main.py:
"""
parser.add_argument('--ocr', action='store_true', 
                   help='Force OCR text extraction (useful for scanned PDFs)')
parser.add_argument('--ocr-lang', default='eng+chi_sim',
                   help='OCR language codes (default: eng+chi_sim)')
parser.add_argument('--ocr-fallback', action='store_true', default=True,
                   help='Automatically use OCR for image-based PDFs')
"""
