#!/usr/bin/env python2


import sys

MORSE_CODE_DICT = { 'A':'.-', 'B':'-...', 
                    'C':'-.-.', 'D':'-..', 'E':'.', 
                    'F':'..-.', 'G':'--.', 'H':'....', 
                    'I':'..', 'J':'.---', 'K':'-.-', 
                    'L':'.-..', 'M':'--', 'N':'-.', 
                    'O':'---', 'P':'.--.', 'Q':'--.-', 
                    'R':'.-.', 'S':'...', 'T':'-', 
                    'U':'..-', 'V':'...-', 'W':'.--', 
                    'X':'-..-', 'Y':'-.--', 'Z':'--..', 
                    '1':'.----', '2':'..---', '3':'...--', 
                    '4':'....-', '5':'.....', '6':'-....', 
                    '7':'--...', '8':'---..', '9':'----.', 
                    '0':'-----', ', ':'--..--', '.':'.-.-.-', 
                    '?':'..--..', '/':'-..-.', '-':'-....-', 
                    '(':'-.--.', ')':'-.--.-'}

MORSE_CODE_DICT = dict((v,k) for k,v in MORSE_CODE_DICT.iteritems())

def level_two_decrypt(enc):
    global MORSE_CODE_DICT
    t = ''
    for c in enc:
        if c == '-':
            t += '.'
        elif c == '.':
            t += '-'
        else:
            t += ' '

    print t
    s = t.split(' ')

    unmorsed = ''.join([MORSE_CODE_DICT[c] for c in s])

    return unmorsed

print level_two_decrypt(sys.argv[1])