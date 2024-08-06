import re

def search_for_flags(text):
    flag_patterns = [
        r'OOO\{.*?\}',
        r'picoCTF\{.*?\}',
        r'CTF\{.*?\}',
        r'flag\{.*?\}',
        r'FLAG\{.*?\}',
        r'[a-zA-Z0-9]{32}',  # Common pattern for MD5 hashes
        # Add more patterns if needed
    ]
    flags = []
    for pattern in flag_patterns:
        matches = re.findall(pattern, text)
        flags.extend(matches)
    return flags

