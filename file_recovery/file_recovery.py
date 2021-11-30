#!/usr/bin/python3

# Authors: Tanner Bonds, Drew Yarbrough
# Professor: Dr. Jason Cuneo
# Assignment: Project 2
# Class: COMP 6350 - Digital Forensics, Auburn University
# Date: November 2021
from argparse import ArgumentParser
import re
import binascii
import struct
import hashlib
import os
import sys


def parse():
    parser = ArgumentParser()
    parser.add_argument('file')
    return parser.parse_args()


def get_hex(filename):

    with open(filename, 'rb') as f:
        raw = f.read()
    return raw


def get_files(raw):
    headers = []
    footers = []
    file_count = 1
    header_skip = False
    footer_skip = False
    pdf_skip = False
    file_signatures = [
        ['.mpg',  b'\x00\x00\x01\xB3.\x00', b'\x00\x00\x00\x01\xB7'],
        ['.mpg',  b'\x00\x00\x01\xBA.\x00', b'\x00\x00\x00\x01\xB9'],
        ['.pdf',  b'\x25\x50\x44\x46', b'\x0A\x25\x25\x45\x4F\x46\x0A'],
        ['.pdf',  b'\x25\x50\x44\x46', b'\x0D\x0A\x25\x25\x45\x4F\x46\x0D\x0A'],
        ['.pdf',  b'\x25\x50\x44\x46', b'\x0A\x25\x25\x45\x4F\x46\x0A'],
        ['.pdf',  b'\x25\x50\x44\x46', b'\x0A\x25\x25\x45\x4F\x46'],
        ['.pdf',  b'\x25\x50\x44\x46', b'\x0D\x25\x25\x45\x4F\x46\x0D'],
        ['.bmp', b'\x42\x4D....\x00\x00\x00\x00', None],
        ['.gif', b'\x47\x49\x46\x38\x37\x61', b'\x00\x00\x3B'],
        ['.gif', b'\x47\x49\x46\x38\x39\x61', b'\x00\x00\x3B'],
        ['.jpg', b'\xFF\xD8\xFF\xE0', b'\xFF\xD9'],
        ['.jpg', b'\xFF\xD8\xFF\xE1', b'\xFF\xD9'],
        ['.jpg', b'\xFF\xD8\xFF\xE2', b'\xFF\xD9'],
        ['.jpg', b'\xFF\xD8\xFF\xE8', b'\xFF\xD9'],
        ['.jpg', b'\xFF\xD8\xFF\xDB', b'\xFF\xD9'],
        ['.docx', b'\x50\x4B\x03\x04\x14\x00\x06\x00', b'\x50\x4B\x05\x06'],
        ['.avi', b'\x52\x49\x46\x46....\x41\x56\x49\x20\x4C\x49\x53\x54', None],
        ['.png', b'\x89\x50\x4E\x47\x0D\x0A\x1A\x0A',
         b'\x49\x45\x4E\x44\xAE\x42\x60\x82']
    ]
    for signature in file_signatures:
        re_header = re.compile(signature[1])
        for header_match in re_header.finditer(raw):
            next_offset = 0
            offset = header_match.start()
            header_skip = False
            if offset in headers:
                header_skip = True
            start = raw[offset:]
            if signature[0] == '.pdf' and header_skip == False:
                for match in re_header.finditer(raw[offset+1:]):
                    next_offset = match.start() + offset
                    break
            if not header_skip:
                if signature[2] is not None:
                    re_footer = re.compile(signature[2])
                    for footer_match in re_footer.finditer(start):
                        next_end = 0
                        pdf_skip = False
                        end = footer_match.end()
                        end += offset
                        if signature[0] == '.pdf':
                            for match in re_footer.finditer(raw[end:]):
                                next_end = match.start() + end
                                break
                            if not next_offset == 0:
                                if end > next_offset:
                                    pdf_skip = True
                                    break
                            elif not next_end == 0:
                                if next_end > next_offset:
                                    break
                        elif signature[0] == '.docx':
                            end += 18
                        else:
                            break
                else:
                    if signature[0] == '.bmp':
                        head = 2
                    elif signature[0] == '.avi':
                        head = 4
                    size_start = head + offset
                    file_size = str(hex(raw[size_start])[2:].zfill(2)) + str(hex(raw[size_start+1])[2:].zfill(
                        2)) + str(hex(raw[size_start+2])[2:].zfill(2)) + str(hex(raw[size_start+3])[2:].zfill(2))
                    size_b = binascii.unhexlify(file_size)
                    size_long = struct.unpack('<l', size_b)
                    end = size_long[0] + offset
                    if signature[0] == '.avi':
                        end += 8
            footer_skip = False
            if end in footers:
                footer_skip = True
            if not (header_skip or footer_skip or pdf_skip):
                headers.append(offset)
                footers.append(end)
                new_file = raw[offset:end]
                if not os.path.exists('./recovered_files'):
                    os.mkdir('./recovered_files')
                if sys.platform.__contains__('win32') or sys.platform.__contains__('cygwin'):
                    file_name = r'recovered_files\file' + \
                        str(file_count) + signature[0]
                    with open(file_name, 'wb') as w:
                        w.write(new_file)
                else:
                    file_name = 'recovered_files/file' + \
                        str(file_count) + signature[0]
                    with open(file_name, 'wb') as w:
                        w.write(new_file)
                with open(file_name, 'rb') as hash_file:
                    data = hash_file.read(65536)
                    hasher = hashlib.sha256(data)
                    while data:
                        data = hash_file.read(65536)
                        hasher.update(data)
                file_hash = hasher.hexdigest()
                file_count += 1

                print('\nFile Name: ' + file_name)
                print('Starting Offset: ' + hex(offset))
                print('Ending Offset: ' + hex(end))
                print('SHA256 Hash: ' + file_hash)


def main():
    args = parse()
    raw = get_hex(args.file)
    get_files(raw)


if __name__ == '__main__':
    main()
