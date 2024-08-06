import subprocess
import logging

def run_command(command):
    logging.info(f"Running command: {command}")
    try:
        output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
        return output.decode('utf-8')
    except subprocess.CalledProcessError as e:
        return f"Error running command: {e.output.decode('utf-8')}"

