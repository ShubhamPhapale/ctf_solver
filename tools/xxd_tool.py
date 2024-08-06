import logging
from utils.flag_utils import search_for_flags
from utils.command_utils import run_command

class XXDTool:
    def analyze(self, file_path, trace):
        xxd_output = run_command(f'xxd {file_path}')
        flags_found = search_for_flags(xxd_output)
        if flags_found:
            trace.append(f"XXD -> {flags_found}")
        return flags_found, trace

