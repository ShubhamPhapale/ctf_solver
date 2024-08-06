import os
import argparse
import shutil
import logging
from config import TOOLS
from utils.file_utils import extract_archive, analyze_recursive

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(message)s')

def main():
    parser = argparse.ArgumentParser(description='Automated Forensics Analysis Tool with Flag Detection')
    parser.add_argument('target', help='File or directory to analyze')
    args = parser.parse_args()

    target = args.target

    if os.path.isfile(target):
        output_dir = 'analysis_output'
        os.makedirs(output_dir, exist_ok=True)
        trace = []
        flags, trace = analyze_recursive(target, output_dir, trace, TOOLS)
        if flags:
            logging.info(f"--- Flag Found ---\n{flags}\n--- Trace ---\n{trace}\n")
        else:
            logging.info("No flags found.")
        shutil.rmtree(output_dir)

    elif os.path.isdir(target):
        all_flags = []
        trace = []
        for root, dirs, files in os.walk(target):
            for file in files:
                file_path = os.path.join(root, file)
                logging.info(f"Analyzing file: {file_path}")
                output_dir = 'analysis_output'
                os.makedirs(output_dir, exist_ok=True)
                flags, file_trace = analyze_recursive(file_path, output_dir, trace, TOOLS)
                if flags:
                    logging.info(f"--- Flag Found ---\n{flags}\n--- Trace ---\n{file_trace}\n")
                    all_flags.extend(flags)
                shutil.rmtree(output_dir)
        if not all_flags:
            logging.info("No flags found in directory.")
    else:
        logging.error("Invalid target specified. Please provide a valid file or directory.")

if __name__ == "__main__":
    main()

