"""
Utility functions for PDF2Word converter
"""

import os
import glob
from pathlib import Path
from datetime import datetime


def generate_unique_filename(output_path: str) -> str:
    """
    Generate a unique filename by adding timestamp if file already exists
    
    Args:
        output_path (str): Desired output file path
        
    Returns:
        str: Unique file path with timestamp if needed
    """
    if not os.path.exists(output_path):
        return output_path
    
    # File exists, add timestamp
    path_obj = Path(output_path)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    new_name = f"{path_obj.stem}_{timestamp}{path_obj.suffix}"
    new_path = path_obj.parent / new_name
    
    print(f"⚠️ File already exists, adding timestamp: {new_name}")
    return str(new_path)


def find_pdf_files(input_path: str) -> list:
    """
    Find PDF files in the given path
    
    Args:
        input_path (str): Directory path or file pattern
        
    Returns:
        list: List of PDF file paths
    """
    pdf_files = []
    
    if os.path.isfile(input_path):
        # Single file
        if input_path.lower().endswith('.pdf'):
            pdf_files.append(input_path)
    elif os.path.isdir(input_path):
        # Directory - find all PDF files
        pattern = os.path.join(input_path, "*.pdf")
        pdf_files.extend(glob.glob(pattern))
        
        # Also search subdirectories if recursive flag is used
        pattern_recursive = os.path.join(input_path, "**", "*.pdf")
        pdf_files.extend(glob.glob(pattern_recursive, recursive=True))
        
        # Remove duplicates
        pdf_files = list(set(pdf_files))
    else:
        # Pattern matching
        pdf_files.extend(glob.glob(input_path))
    
    return sorted(pdf_files)
