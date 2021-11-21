from argparse import ArgumentParser
import binascii


def parse():
    parser = ArgumentParser()
    parser.add_argument('file')
    return parser.parse_args()


def get_hex(filename):

    with open(filename, 'rb') as f:
        hex_data = str(binascii.hexlify(f.read()))
    return hex_data


def get_files(hex):

    file_sigs = {'25504446': 'pdf'}
    pdf_trailers = ['0a2525454f46', '0a2525454f460a',
                    '0d0a2525454f460d0a', '0d2525454f460d']
    file_info = []
    header = ''
    trailer_value = ''
    file_data = ''
    for key in file_sigs.keys():
        header = hex.find(key)
        if not header == '':
            for trailer in pdf_trailers:
                trailer_value = hex.find(trailer)
                if not trailer_value == '':
                    file_data = hex[header:trailer_value] + trailer
                    file_info.append(file_data)
                    header = ''
                    trailer_value = ''
                    file_data = ''
                    break
    print(file_info)


def main():
    args = parse()
    hex = get_hex(args.file)
    get_files(hex)


if __name__ == '__main__':
    main()
