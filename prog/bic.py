import os
import sys
from PIL import Image
import argparse
import argparse
# Usage: python bulk_webp_converter.py <folder_path> <output_format> <rename> <generate_sizes>


def convert_images(folder_path, output_format, rename=None, generate_sizes=None):
    '''
    Converts all images in a folder to the specified format
    folder_path: Path to the folder containing the images
    output_format: The format to which the images should be converted
    rename: If specified, the converted images will be renamed to the specified name
    generate_sizes: If specified, the converted images will be resized to the specified percentages

    Example:
    python bulk_webp_converter.py C:/Users/username/Desktop/images -webp -rename=converted -generatesizes [45,60,75,90]

    '''
    print(folder_path, output_format, rename, generate_sizes)
    count = 1

    output_folder = os.path.join(folder_path, 'Output').replace("\\", "/")
    print(output_folder)
    while os.path.exists(output_folder):
        count += 1
        output_folder = os.path.join(
            folder_path, f'Output{count}').replace("\\", "/")
    os.makedirs(output_folder, exist_ok=True)

    format_map = {'webp': 'webp', 'jpeg': 'jpeg', 'png': 'png'}

    count = 1
    for filename in sorted(os.listdir(folder_path)):
        print(filename)
        if filename.endswith('.jpg') or filename.endswith('.jpeg') or filename.endswith('.png') or filename.endswith('.webp'):
            img_path = os.path.join(folder_path, filename).replace("\\", "/")
            img = Image.open(img_path)
            if(format_map[output_format] == 'jpeg'):
                print("hi")
                img = img.convert('RGB')
                print(img.mode)

            output_path = os.path.join(
                output_folder, filename.split('.')[0]) + '.' + format_map[output_format]
            output_path = output_path.replace("\\", "/")
            print("OUTPUT", output_path)
            if rename:
                output_path = os.path.join(
                    output_folder, f'{rename}_{count}.').replace("\\", "/") + format_map[output_format]

            if os.path.exists(output_path):
                print(f'{output_path} already exists')
            else:
                img.save(output_path, format_map[output_format])
            print(f'{img_path} converted to {output_path}')

            if generate_sizes:
                generate_resized_images(
                    output_path, output_format, generate_sizes)
        # else:
        #     print(f'Invalid output format: {output_format}')
        #     return
        count += 1

# Generates resized images of the specified percentages


def generate_resized_images(img_path, output_format, generate_sizes):
    '''
    Generates resized images of the specified percentages
    img_path: Path to the image
    output_format: The format to which the images should be converted
    generate_sizes: The percentages to which the images should be resized

    Example:
    python bulk_webp_converter.py C:/Users/username/Desktop/images -webp -rename=converted -generatesizes [45,60,75,90]



    '''
    img = Image.open(img_path)
    for size in generate_sizes:
        width, height = img.size
        new_width = int(width * size / 100)
        new_height = int(height * size / 100)
        resized_img = img.resize((new_width, new_height))
        resized_path = f'{img_path}'.split(
            '.')[0]+f'_perc_{size}.{output_format}'

        if os.path.exists(resized_path):
            print(f'{resized_path} already exists')
            continue
        resized_img.save(resized_path, output_format)


def comma_seperated(string):
    if string:
        for size in string.split(','):
            if not size.isdigit():
                raise argparse.ArgumentTypeError(
                    "Comma seperated list of integers expected")
    else:
        raise argparse.ArgumentTypeError(
            "Comma seperated list of integers expected")

    return [int(size) for size in string.split(',')]


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Converts all images in a folder to the specified format')
    parser.add_argument('folder_path', type=str,
                        help='Path to the folder containing the images')
    parser.add_argument('-f', '--format', type=str, choices=[
                        'webp', 'jpeg', 'png'], help='The format to which the images should be converted')
    parser.add_argument('-r', '--rename', type=str, nargs='?',
                        help='If specified, the converted images will be renamed to the specified name')
    parser.add_argument('-s', '--sizes', type=comma_seperated, nargs=1,
                        help='If specified, the converted images will be resized to the specified percentages')

    args = parser.parse_args()
    print(args)
    if not args.format:
        print('Output format not specified')
    else:
        convert_images(args.folder_path, args.format,
                       args.rename, args.sizes)
