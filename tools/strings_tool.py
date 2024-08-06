import logging
from utils.flag_utils import search_for_flags
from utils.command_utils import run_command

class StringsTool:
    def analyze(self, file_path, trace):
        strings_output = run_command(f'strings {file_path}')
        flags_found = search_for_flags(strings_output)
        if flags_found:
            trace.append(f"Strings -> {flags_found}")
        return flags_found, trace

