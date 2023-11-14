import os
import sys
from PIL import Image
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

    count = 1
    print(rename)
    output_folder = os.path.join(folder_path, 'Output').replace("\\", "/")
    while os.path.exists(output_folder):
        count += 1
        output_folder = os.path.join(
            folder_path, f'Output{count}').replace("\\", "/")
    os.makedirs(output_folder, exist_ok=True)

    format_map = {'webp': 'webp', 'jpg': 'jpeg', 'png': 'png'}

    count = 1
    for filename in sorted(os.listdir(folder_path)):
        if filename.endswith('.jpg') or filename.endswith('.jpeg') or filename.endswith('.png') or filename.endswith('.webp'):
            img_path = os.path.join(folder_path, filename).replace("\\", "/")
            img = Image.open(img_path)

            if output_format in format_map:
                if not filename.endswith('.' + format_map[output_format]):
                    output_path = os.path.join(
                        output_folder, filename.split('.')[0]) + '.' + format_map[output_format]
                    output_path = output_path.replace("\\", "/")
                    print(output_path)
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
            else:
                print(f'Invalid output format: {output_format}')
                return
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


if __name__ == '__main__':
    folder_path = sys.argv[1]
    output_format = None
    rename = None
    generate_sizes = None

    for i, arg in enumerate(sys.argv[2:]):
        if arg == '--webp':
            if output_format:
                print(
                    f'Output format already specified, should not pass multiple output formats -{output_format}, {arg}')
                exit(1)

            output_format = 'webp'
        elif arg == '--jpg':
            if output_format:
                print(
                    f'Output format already specified, should not pass multiple output formats -{output_format}, {arg}')
                exit(1)

            output_format = 'jpg'
        elif arg == '--png':
            if output_format:
                print(
                    f'Output format already specified, should not pass multiple output formats -{output_format}, {arg}')
                exit(1)

            output_format = 'png'
        elif arg.startswith('--rename='):
            rename = arg.split('=')[1]

        elif arg == '--generatesizes':
            generate_sizes = [45, 60, 75, 90]
        elif arg.startswith('-generatesizes='):
            sizes = sys.argv[i+3]
            if (not sizes.startswith('[') and not sizes.endswith(']')):
                print('Invalid size list')
                break
            sizes = sizes.replace('[', '').replace(']', '')

            generate_sizes = [int(size) for size in sizes.split(',')]
    if not output_format:
        print('Output format not specified')
    else:
        convert_images(folder_path, output_format, rename, generate_sizes)
