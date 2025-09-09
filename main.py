import os
import sys
from pathlib import Path
from pdf2docx import Converter
import argparse
import glob
from concurrent.futures import ThreadPoolExecutor, as_completed
import time


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
        print(f"🔄 Converting {Path(pdf_path).name} to {Path(output_path).name}...")
        cv = Converter(pdf_path)
        cv.convert(output_path, start=0, end=None)
        cv.close()
        print(f"✅ Conversion completed: {Path(output_path).name}")
        return str(output_path)
        
    except Exception as e:
        print(f"❌ Error converting {Path(pdf_path).name}: {str(e)}")
        raise


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


def main():
    """Main function with command line interface"""
    parser = argparse.ArgumentParser(
        description='Convert PDF to Word document - supports single files, directories, and batch processing',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # 批量转换 input/ 文件夹中的所有PDF文件到 output/ 文件夹
  uv run main.py
  
  # 转换单个文件
  uv run main.py document.pdf
  
  # 转换单个文件并指定输出位置
  uv run main.py document.pdf -o output.docx
  
  # 指定线程数进行批量转换
  uv run main.py --threads 8
        """
    )
    
    parser.add_argument('input', nargs='?', default='input/',
                       help='PDF file, directory containing PDFs, or file pattern (default: input/)')
    parser.add_argument('-o', '--output', default='output/',
                       help='Output file path (for single file) or output directory (default: output/)')
    parser.add_argument('--threads', type=int, default=4, 
                       help='Number of threads for batch processing (default: 4)')
    parser.add_argument('--version', action='version', version='PDF2Word 2.0.0')
    
    args = parser.parse_args()
    
    # 确保默认目录存在
    script_dir = Path(__file__).parent
    input_dir = script_dir / "input"
    output_dir = script_dir / "output"
    
    input_dir.mkdir(exist_ok=True)
    output_dir.mkdir(exist_ok=True)
    
    try:
        # Find PDF files
        pdf_files = find_pdf_files(args.input)
        
        if not pdf_files:
            print(f"❌ No PDF files found in: {args.input}")
            print("\n💡 使用说明:")
            print(f"   1. 将PDF文件放入 {input_dir} 文件夹")
            print(f"   2. 运行 'uv run main.py' 开始批量转换")
            print(f"   3. 转换完成的Word文档将保存到 {output_dir} 文件夹")
            print("\n   或者直接指定PDF文件路径:")
            print("   uv run main.py your_file.pdf")
            return 1
        
        if len(pdf_files) == 1 and os.path.isfile(args.input):
            # Single file conversion (only when user specified a file directly)
            print(f"📄 Converting single file: {pdf_files[0]}")
            
            # For single file, if output is a directory, generate filename
            if os.path.isdir(args.output) or args.output == 'output/':
                output_file_path = os.path.join(args.output, Path(pdf_files[0]).with_suffix('.docx').name)
            else:
                output_file_path = args.output
                
            output_file = pdf_to_word(pdf_files[0], output_file_path)
            print(f"✅ Successfully converted to: {output_file}")
            return 0
        else:
            # Batch conversion (including single file found in directory)
            print(f"🚀 Starting batch conversion...")
            print(f"📁 Input: {args.input}")
            print(f"📁 Output: {args.output}")
            results = batch_convert(pdf_files, args.output, args.threads)
            
            if results["failed"] > 0:
                print(f"\n⚠️ Some conversions failed:")
                for file_result in results["files"]:
                    if file_result["status"] == "failed":
                        print(f"   ❌ {Path(file_result['input']).name}: {file_result['error']}")
                return 1
            else:
                print(f"\n🎉 All conversions completed successfully!")
                return 0
                
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
