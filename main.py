#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from plagiarism import readfile, getkeywords, evaluate, timestr


langs = ["english"]

def writelog(log, file1, keywords1, file2, keywords2, blocks, local = False):
    log.write("=" * 30 + "\n")
    log.write("Source file: " + file1 + "\n")
    log.write("Keywords 1: " + ", ".join(keywords1) + "\n")
    if local:
        log.write("Source file 2: " + file2 + "\n")
    else:
        log.write("Googled file: " + file2 + "\n")
    log.write("Keywords 2: " + ", ".join(keywords2) + "\n")
    for ssk, s, t in blocks:
        log.write("-" * 30 + "\n")
        log.write("Plagiated block with ssk: " + "%0.5f\n" % ssk)
        log.write("Source: " + " ".join(s) + "\n")


def main(argc, argv):
    if argc < 2:
        print("No input file specified")
        return

    if argv[1]:
        text = readfile(argv[1])
    if text == None:
        print("File don't exist or extension eror")
        return

    log = open("log.txt", 'w')

    if (argc == 3):
        if argv[2]:
            text2 = readfile(argv[2])
            keywords = getkeywords(text, langs=langs)
            keywords2 = getkeywords(text2, langs=langs)
            print("Keywords for text 1: ", ", ".join(keywords))
            print("Keywords for text 2: ", ", ".join(keywords2))
            print("Searching for plagiated blocks ({0})".format(timestr()))
            blocks = evaluate(text, text2, langs=langs, debug=False)
            print("Search ended, found {0} plagiated blocks ({1})".format(len(blocks), timestr()))
            if len(blocks) > 0:
                writelog(log, argv[1], keywords, argv[2], keywords2, blocks, local=True)
                print("\nAll plagiated blocks were written to log.txt")
        log.close()
        return

    keywords = getkeywords(text, langs=langs)
    print("Keywords for source: " + ", ".join(keywords))


    print("\nAll plagiated blocks were written to log.txt")
    log.close()

if __name__ == "__main__":
    main(len(sys.argv), sys.argv)
