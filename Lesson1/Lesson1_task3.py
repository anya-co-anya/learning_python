#!/usr/bin/python3


def main():
    nine_hashes = '#'*9 + '\n'
    two_hashes = '#' + '\t'*2 + '#' + '\n'

    print(nine_hashes, two_hashes*3, nine_hashes, sep='')
    print(two_hashes*2, nine_hashes, two_hashes*2, sep='')


main()


