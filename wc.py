
import argparse
import sys
import re


def printWc(line_count, word_count, char_count, filename):
    print(f"{line_count:8}{word_count:8}{char_count:8} {filename or ''}")


def wc(filenameList=None):

    total_lines, total_words, total_chars, total_sentences, total_paragraphs = 0, 0, 0, 0, 0
    if filenameList:
        for filename in filenameList:

            with open(filename, 'r') as file:
                contents = file.read()
                print(type(contents))
                lines = contents.split('\n')
                words = re.findall(r'\b\w+\b', contents)
                chars = len(contents)
                sentences = re.findall(r'[^\s][^.?!]*[.?!]', contents)
                paragraphs = re.split('\n{2,}', contents)
                printWc(len(lines), len(words), chars, filename)
                total_lines += len(lines)
                total_words += len(words)
                total_chars += chars
                total_sentences += len(sentences)
                total_paragraphs += len(paragraphs)

        if len(filenameList) > 1:
            printWc(total_lines, total_words, total_chars, 'total')

    else:
        contents = "".join([x for x in sys.stdin])
        print(contents)
        lines = contents.split('\n')
        words = re.findall(r'\b\w+\b', contents)
        chars = len(contents)
        sentences = re.findall(r'[^\s][^.?!]*[.?!]', contents)
        paragraphs = re.split('\n{2,}', contents)
        printWc(len(lines), len(words), chars, None)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Word count utility')
    parser.add_argument('filename', nargs='*',
                        help='File to count (optional, if omitted, reads from stdin)')

    args = parser.parse_args()
    wc(args.filename)
