"""
Core conversion functions for PDF2Word converter
"""

import os
import time
from pathlib import Path
from pdf2docx import Converter
from concurrent.futures import ThreadPoolExecutor, as_completed

from .utils import generate_unique_filename


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
    
    # Generate unique filename to avoid overwriting existing files
    output_path = generate_unique_filename(output_path)
    
    # Ensure output directory exists
    output_dir = Path(output_path).parent
    output_dir.mkdir(parents=True, exist_ok=True)
    
    try:
        # Convert PDF to Word
        print(f"🔄 Converting {Path(pdf_path).name} to {Path(output_path).name}...")
        cv = Converter(pdf_path)
        cv.convert(output_path, start=0, end=None)
        cv.close()
        print(f"✅ Conversion completed: {Path(output_path).name}")
        return str(output_path)
        
    except Exception as e:
        print(f"❌ Error converting {Path(pdf_path).name}: {str(e)}")
        raise


def convert_single_file(pdf_path: str, output_dir: str = None) -> tuple:
    """
    Convert a single PDF file (for use with threading)
    
    Args:
        pdf_path (str): Path to PDF file
        output_dir (str): Output directory
        
    Returns:
        tuple: (pdf_path, success, output_path_or_error)
    """
    try:
        if output_dir:
            output_path = os.path.join(output_dir, Path(pdf_path).with_suffix('.docx').name)
        else:
            output_path = None
            
        result = pdf_to_word(pdf_path, output_path)
        return (pdf_path, True, result)
    except Exception as e:
        return (pdf_path, False, str(e))


def batch_convert(pdf_files: list, output_dir: str = None, max_workers: int = 4) -> dict:
    """
    Convert multiple PDF files using threading
    
    Args:
        pdf_files (list): List of PDF file paths
        output_dir (str): Output directory for converted files
        max_workers (int): Maximum number of threads
        
    Returns:
        dict: Results summary
    """
    if not pdf_files:
        print("❌ No PDF files found to convert")
        return {"success": 0, "failed": 0, "files": []}
    
    print(f"📚 Found {len(pdf_files)} PDF files to convert")
    print(f"🧵 Using {max_workers} threads for conversion")
    
    if output_dir:
        os.makedirs(output_dir, exist_ok=True)
        print(f"📁 Output directory: {output_dir}")
    
    results = {"success": 0, "failed": 0, "files": []}
    start_time = time.time()
    
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        # Submit all conversion tasks
        future_to_pdf = {
            executor.submit(convert_single_file, pdf_path, output_dir): pdf_path 
            for pdf_path in pdf_files
        }
        
        # Process completed tasks
        for future in as_completed(future_to_pdf):
            pdf_path, success, result = future.result()
            
            if success:
                results["success"] += 1
                results["files"].append({"input": pdf_path, "output": result, "status": "success"})
            else:
                results["failed"] += 1
                results["files"].append({"input": pdf_path, "error": result, "status": "failed"})
    
    end_time = time.time()
    duration = end_time - start_time
    
    # Print summary
    print("\n" + "="*50)
    print(f"📊 Conversion Summary:")
    print(f"✅ Successful: {results['success']}")
    print(f"❌ Failed: {results['failed']}")
    print(f"⏱️ Total time: {duration:.2f} seconds")
    print("="*50)
    
    return results
