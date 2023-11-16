
import argparse
import sys
import re
import os

def wc(filenameList=None, line_flag=False, word_flag=False, char_flag=False):
    def printWc(line_count, word_count, char_count, filename):
        '''
        Prints the word count in the format:
        <line_count> <word_count> <char_count> <filename> depending on the flags

        Example:

        python wc.py test.txt
        1       2       12      test.txt

        python wc.py -l -w -c test.txt test2.txt
        1       2       12      test.txt
        1       2       12      test2.txt

        python wc.py -lw test.txt test2.txt test3.txt

        1       2       test.txt
        1       2       test2.txt
        1       2       test3.txt


        '''

        if line_flag:
            print(f"{line_count:8}", end='')

        if word_flag:
            print(f"{word_count:8}", end='')

        if char_flag:
            print(f"{char_count:8}", end='')

        if filename:
            print(f" {filename}")

    total_lines, total_words, total_chars, total_sentences = 0, 0, 0, 0
    if filenameList:
        for filename in filenameList:

            with open(filename, 'r') as file:
                contents = file.read()
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

        if len(filenameList) > 1:
            printWc(total_lines, total_words, total_chars, 'total')

    else:
        contents = "".join([x for x in sys.stdin])

        lines = contents.split('\n')
        words = re.findall(r'\b\w+\b', contents)
        chars = len(contents)
        sentences = re.findall(r'[^\s][^.?!]*[.?!]', contents)

        printWc(len(lines), len(words), chars, None)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Word count utility')
    parser.add_argument('filename', nargs='*',
                        help='File to count (optional if not provided reads from stdin)')
    parser.add_argument('-l', '--lines', action='store_true',
                        help='Count lines')
    parser.add_argument('-w', '--words', action='store_true',
                        help='Count words')
    parser.add_argument('-c', '--chars', action='store_true',
                        help='Count chars')

    args = parser.parse_args()
    if not (args.lines or args.words or args.chars):
        args.lines, args.words, args.chars = True, True, True

    wc(args.filename, args.lines, args.words, args.chars)
