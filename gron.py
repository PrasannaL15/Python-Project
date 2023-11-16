# json = {};
# json.menu = {};
# json.menu.id = "file";
# json.menu.popup = {};
# json.menu.popup.menuitem = [];
# json.menu.popup.menuitem[0] = {};
# json.menu.popup.menuitem[0].onclick = "CreateNewDoc()";
# json.menu.popup.menuitem[0].value = "New";
# json.menu.popup.menuitem[1] = {};
# json.menu.popup.menuitem[1].onclick = "OpenDoc()";
# json.menu.popup.menuitem[1].value = "Open";
# json.menu.popup.menuitem[2] = {};
# json.menu.popup.menuitem[2].onclick = "CloseDoc()";
# json.menu.popup.menuitem[2].value = "Close";
# json.menu.value = "File";
import json
import sys
import argparse


def do_gron(data, obj):
    """Convert JSON to gron format"""

    output = ''
    for key, value in sorted(data.items(), key=lambda x: x[0]):
        output += f'{obj}'
        if isinstance(value, dict):
            output += f'.{key} = {{}}\n'
            output += do_gron(value, f'{obj}.{key}')
        elif isinstance(value, list):
            output += f'.{key} = []\n'
            for i, item in enumerate(value):
                output += f'{obj}.{key}[{i}] = {{}}\n'
                output += do_gron(item, f'{obj}.{key}[{i}]')
        else:
            output += f'.{key} = {json.dumps(value)}\n'
    return output


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Gron utility')
    parser.add_argument('filename', nargs='?',
                        help='File to count (optional, if omitted, reads from stdin)')
    parser.add_argument('--obj', nargs='?', default='json',
                        help='Specify base object (default: json)')

    args = parser.parse_args()

    if args.filename:
        with open(args.filename, 'r') as f:
            data = json.load(f)
    else:
        data = json.load(sys.stdin)

    output = do_gron(data, args.obj)
    print(f"{args.obj} = {{}}\n{output if output else None}")
