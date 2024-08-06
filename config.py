from tools.binwalk_tool import BinwalkTool
from tools.strings_tool import StringsTool
from tools.exiftool_tool import ExiftoolTool
from tools.steghide_tool import SteghideTool
from tools.zsteg_tool import ZstegTool
from tools.ocr_tool import OCRTool
from tools.foremost_tool import ForemostTool
from tools.xxd_tool import XXDTool
from tools.radare2_tool import Radare2Tool

TOOLS = [
    BinwalkTool(),
    StringsTool(),
    ExiftoolTool(),
    SteghideTool(),
    ZstegTool(),
    OCRTool(),
    ForemostTool(),
    XXDTool(),
    Radare2Tool()
]

