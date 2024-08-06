import logging
from PIL import Image
import pytesseract
from utils.flag_utils import search_for_flags

class OCRTool:
    def analyze(self, file_path, trace):
        flags_found = []
        try:
            ocr_text = pytesseract.image_to_string(Image.open(file_path))
            flags_found = search_for_flags(ocr_text)
            if flags_found:
                trace.append(f"OCR -> {flags_found}")
        except Exception as e:
            logging.info(f"OCR Error: {e}")
        return flags_found, trace

