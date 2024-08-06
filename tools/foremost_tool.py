import logging
from utils.flag_utils import search_for_flags
from utils.command_utils import run_command

class ForemostTool:
    def analyze(self, file_path, trace):
        foremost_output = run_command(f'foremost -i {file_path} -o foremost_output')
        flags_found = search_for_flags(foremost_output)
        if flags_found:
            trace.append(f"Foremost -> {flags_found}")
        return flags_found, trace

