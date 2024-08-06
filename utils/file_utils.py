import os
import tarfile
import zipfile
import logging
from utils.command_utils import run_command
from utils.flag_utils import search_for_flags

def extract_archive(file_path, extract_to):
    if tarfile.is_tarfile(file_path):
        with tarfile.open(file_path) as tar:
            tar.extractall(path=extract_to)
    elif zipfile.is_zipfile(file_path):
        with zipfile.ZipFile(file_path, 'r') as zip_ref:
            zip_ref.extractall(extract_to)
    else:
        return False
    return True

def analyze_recursive(file_path, output_dir, trace, tools):
    for tool in tools:
        flags, trace = tool.analyze(file_path, trace)
        if flags:
            return flags, trace

    if extract_archive(file_path, output_dir):
        for root, dirs, files in os.walk(output_dir):
            for file in files:
                nested_file_path = os.path.join(root, file)
                logging.info(f"Analyzing nested file: {nested_file_path}")
                nested_flags, nested_trace = analyze_recursive(nested_file_path, os.path.join(output_dir, 'nested'), trace, tools)
                if nested_flags:
                    return nested_flags, nested_trace

    return [], trace

