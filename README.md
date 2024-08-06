# CTF Solver

CTF Solver is an automated tool designed to assist in solving Capture The Flag (CTF) forensics challenges. It leverages a variety of tools and techniques to analyze files and directories, including archives, images, text files, and binary data. The tool applies multiple methods to extract hidden flags and provides a detailed trace of the analysis process.

## Features

- **Recursive Analysis**: Handles nested archives and analyzes files at multiple levels.
- **Tool Integration**: Utilizes popular forensic tools like Binwalk, Strings, Exiftool, Steghide, Zsteg, Foremost, Xxd, and Radare2.
- **Image Analysis**: Supports OCR and steganographic analysis for image files.
- **Verbose Logging**: Provides detailed logging of commands run and analysis results.
- **Flexible**: Works with various file types and structures.

## Installation

### Prerequisites

- Python 3.x
- Required Python packages: `pillow`, `pytesseract`
- External tools: `binwalk`, `strings`, `exiftool`, `steghide`, `zsteg`, `foremost`, `xxd`, `radare2`

### Installation Steps

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/ctf_solver.git
   cd ctf_solver
   ```

2. **Set Up the Python Environment**

   Create and activate a virtual environment (optional but recommended):

   ```bash
   python -m venv ctfEnv
   source ctfEnv/bin/activate  # On Windows, use `ctfEnv\Scripts\activate`
   ```

3. **Install Required Python Packages**

   ```bash
   pip install -r requirements.txt
   ```

4. **Install External Tools**

   Ensure the following tools are installed on your system. You can use package managers like `apt` for Ubuntu or `brew` for macOS to install them.

   ```bash
   sudo apt-get install binwalk exiftool steghide foremost xxd radare2
   gem install zsteg  # Ruby gem for zsteg
   ```

   For OCR functionality, install Tesseract:

   ```bash
   sudo apt-get install tesseract-ocr
   ```

## Usage

### Basic Command

To analyze a file or directory, use:

```bash
python main.py <target_file_or_directory>
```

### Examples

1. **Analyzing a Single File**

   ```bash
   python main.py example_file.tar
   ```

2. **Analyzing a Directory**

   ```bash
   python main.py example_directory/
   ```

### Output

The tool will output the following:
- **Command Execution Logs**: Commands run during the analysis.
- **Flags Found**: List of detected flags.
- **Trace**: Detailed trace of the steps taken to find the flags.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue for suggestions and improvements.

1. Fork the Repository
2. Create a Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit Your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [Pillow](https://python-pillow.org/) for image processing
- [Pytesseract](https://github.com/madmaze/pytesseract) for OCR
- [Binwalk](https://github.com/ReFirmLabs/binwalk) for firmware analysis
- [Exiftool](https://exiftool.org/) for metadata extraction
- [Steghide](http://steghide.sourceforge.net/) for steganographic analysis
- [Zsteg](https://github.com/zed-0xff/zsteg) for PNG steganographic analysis
- [Foremost](http://foremost.sourceforge.net/) for file carving
- [Xxd](https://linux.die.net/man/1/xxd) for hexadecimal dumps
- [Radare2](https://rada.re/n/) for binary analysis

## Contact

For any questions or support, please contact [shubhamphapale10+github@gmail.com](mailto:shubhamphapale10+github@gmail.com).
