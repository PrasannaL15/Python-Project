
import sys
import re


def wc(filename):
    with open(filename, 'r') as file:
        contents = file.read()
        lines = contents.split('\n')
        words = re.findall(r'\b\w+\b', contents)
        chars = len(contents)
        sentences = re.findall(r'[^\s][^.?!]*[.?!]', contents)
        paragraphs = re.split('\n{2,}', contents)
        print(f"{len(lines):>7} {len(words):>7} {len(sentences):>7} {len(paragraphs):>7} {chars:>7} {filename}")


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python wc.py <filename>")
        sys.exit(1)
    wc(sys.argv[1])
