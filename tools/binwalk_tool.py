import logging
from utils.flag_utils import search_for_flags
from utils.command_utils import run_command

class BinwalkTool:
    def analyze(self, file_path, trace):
        binwalk_output = run_command(f'binwalk {file_path}')
        flags_found = search_for_flags(binwalk_output)
        if flags_found:
            trace.append(f"Binwalk -> {flags_found}")
        return flags_found, trace


