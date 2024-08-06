import logging
from utils.flag_utils import search_for_flags
from utils.command_utils import run_command

class ExiftoolTool:
    def analyze(self, file_path, trace):
        exiftool_output = run_command(f'exiftool {file_path}')
        flags_found = search_for_flags(exiftool_output)
        if flags_found:
            trace.append(f"Exiftool -> {flags_found}")
        return flags_found, trace

