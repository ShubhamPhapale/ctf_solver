import logging
from utils.flag_utils import search_for_flags
from utils.command_utils import run_command

class ZstegTool:
    def analyze(self, file_path, trace):
        zsteg_output = run_command(f'zsteg {file_path}')
        flags_found = search_for_flags(zsteg_output)
        if flags_found:
            trace.append(f"Zsteg -> {flags_found}")
        return flags_found, trace

