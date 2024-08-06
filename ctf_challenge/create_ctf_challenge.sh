#!/bin/bash

# Create directory structure
mkdir -p ctf_challenge
cd ctf_challenge

# Create text file with flag
echo "CTF{this_is_a_sample_flag}" > textfile_with_flag.txt

# Create a simple PNG image (1x1 pixel, red)
echo -e "\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x01\x00\x00\x00\x01\x08\x02\x00\x00\x00\x90wS\xde\x00\x00\x00\x0cIDATx\x9cc\xf8\xff\xff?\x00\x05\xfe\x02\xfe\xdc\xcc\xec\xf1\x00\x00\x00\x00IEND\xaeB\`\x82" > image_with_stego.png

# Embed a hidden message in the PNG (this is a simplistic steganography example)
echo "picoCTF{hidden_in_image}" >> image_with_stego.png

# Create a binary file with some hidden data
echo -e "This is a binary file.\nHidden flag: CTF{binary_flag_found}\nMore random data..." > randomfile.bin

# Create nested archives
tar -cvf nested2.tar image_with_stego.png textfile_with_flag.txt randomfile.bin
tar -cvf nested1.tar nested2.tar
tar -cvf lost_and_found.tar nested1.tar

# Clean up
rm -rf nested1.tar nested2.tar image_with_stego.png textfile_with_flag.txt randomfile.bin

echo "CTF challenge 'lost_and_found.tar' created successfully!"
