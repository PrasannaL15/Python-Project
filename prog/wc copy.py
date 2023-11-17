
import argparse
import sys
import re
import os





def wc(file=None, line_flag=False, word_flag=False, char_flag=False):

    def printWc(line_count, word_count, char_count, filename):
        '''
        Prints the word count in the format:
        <line_count> <word_count> <char_count> <filename> depending on the flags

        Example:

        python wc.py test.txt
        1       2       12      test.txt

        python wc.py -lwc test.txt
        1       2       12      test.txt

        '''

        if line_flag:
            print(f"{line_count:8}", end='')

        if word_flag:
            print(f"{word_count:8}", end='')

        if char_flag:
            print(f"{char_count:8}", end='')

        if filename:
            print(f" {filename}")


    lines, words, chars = 0, 0, 0
    for line in file:
        print(line)
        lines += 1      
        words += len(line.split('\n'))
        chars += len(line)
       
        printWc(lines, words, chars, file.name)
   

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Word count utility')
    parser.add_argument('file', nargs='?', type=argparse.FileType('r'), default=sys.stdin,
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

    wc(args.file, args.lines, args.words, args.chars)
