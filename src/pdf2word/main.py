"""
Main entry point for PDF2Word converter
"""

import os
import sys
import argparse
from pathlib import Path

from .converter import pdf_to_word, batch_convert
from .utils import find_pdf_files


def main():
    """Main function with command line interface"""
    parser = argparse.ArgumentParser(
        description='Convert PDF to Word document - supports single files, directories, and batch processing',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # 批量转换 input/ 文件夹中的所有PDF文件到 output/ 文件夹
  uv run -m pdf2word
  
  # 转换单个文件
  uv run -m pdf2word document.pdf
  
  # 转换单个文件并指定输出位置
  uv run -m pdf2word document.pdf -o output.docx
  
  # 指定线程数进行批量转换
  uv run -m pdf2word --threads 8
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
    # Get the project root directory (go up from src/pdf2word/)
    current_dir = Path(__file__).parent
    project_root = current_dir.parent.parent
    input_dir = project_root / "input"
    output_dir = project_root / "output"
    
    input_dir.mkdir(exist_ok=True)
    output_dir.mkdir(exist_ok=True)
    
    try:
        # Find PDF files
        pdf_files = find_pdf_files(args.input)
        
        if not pdf_files:
            print(f"❌ No PDF files found in: {args.input}")
            print("\n💡 使用说明:")
            print(f"   1. 将PDF文件放入 {input_dir} 文件夹")
            print(f"   2. 运行 'uv run -m pdf2word' 开始批量转换")
            print(f"   3. 转换完成的Word文档将保存到 {output_dir} 文件夹")
            print("\n   或者直接指定PDF文件路径:")
            print("   uv run -m pdf2word your_file.pdf")
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
