"""
PDF2Word - PDF to Word Document Converter

A Python-based PDF to Word document conversion tool with batch processing,
multi-threading support, and smart duplicate handling.
"""

__version__ = "2.0.0"
__author__ = "dpviivqb"
__email__ = ""
__description__ = "PDF to Word Document Converter with batch processing support"

from .converter import pdf_to_word, batch_convert
from .utils import find_pdf_files, generate_unique_filename

__all__ = [
    "pdf_to_word",
    "batch_convert", 
    "find_pdf_files",
    "generate_unique_filename"
]
