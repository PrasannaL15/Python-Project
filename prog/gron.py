
import json
import sys
import argparse


def do_gron(data, obj):
    """Convert JSON to gron format"""

    output = ''
    if isinstance(data,dict):
        for key, value in sorted(data.items(), key=lambda x: x[0]):
            output += f'{obj}'
            if isinstance(value, dict):
                output += f'.{key} = {{}}\n'
                output += do_gron(value, f'{obj}.{key}')
            elif isinstance(value, list):
                output += f'.{key} = []\n'
                for i, item in enumerate(value):
                    output += f'{obj}.{key}[{i}] = '
                    if(isinstance(item,dict)):
                        output+='{}\n'
                    output += do_gron(item, f'{obj}.{key}[{i}]')
            else:
                output += f'.{key} = {json.dumps(value)}\n'
        return output
    else:
        return str(data)+"\n"

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
    if data == []:
        print(f"{args.obj} = []\n")
        exit(0)
    output = do_gron(data, args.obj)
    print(f"{args.obj} = {{}}\n{output if output else ''}")



