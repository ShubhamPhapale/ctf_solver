import os
from utils.command_utils import run_command
from utils.flag_utils import search_for_flags

class SteghideTool:
    def analyze(self, file_path, trace):
        flags_found = []  # Initialize flags_found to an empty list
        if file_path.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp')):
            steghide_output_file = 'steghide_output.txt'
            steghide_output = run_command(f'steghide extract -sf {file_path} -p "" -xf {steghide_output_file}')
            if os.path.exists(steghide_output_file):
                with open(steghide_output_file, 'r', errors='ignore') as f:
                    content = f.read()
                    flags_found = search_for_flags(content)
                    trace.append(f"Steghide -> {flags_found}")
                os.remove(steghide_output_file)
        return flags_found, trace

