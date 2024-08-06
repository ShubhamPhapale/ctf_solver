import logging
from utils.flag_utils import search_for_flags
from utils.command_utils import run_command

class Radare2Tool:
    def analyze(self, file_path, trace):
        radare2_output = run_command(f'r2 -c "aaa; pdd" {file_path}')
        flags_found = search_for_flags(radare2_output)
        if flags_found:
            trace.append(f"Radare2 -> {flags_found}")
        return flags_found, trace

