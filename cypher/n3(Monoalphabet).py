import random
__author__ = 'Timofey Khirianov'
# -*- coding: utf8 -*-


class Monoalphabet:

    alphabet = list("егпжонщюэбэчмяхыцилдшарсйзвьёктф")

    def __init__(self, keytable):
        lowercase_code = {self.alphabet[i]: keytable[i] for i in range(len(self.alphabet))}
        uppercase_code = {self.alphabet[i].upper(): keytable[i].upper() for i in range(len(self.alphabet))}
        self._encode = dict(lowercase_code)
        self._encode.update(uppercase_code)
        Lowercase_code = {keytable[i]: self.alphabet[i] for i in range(len(self.alphabet))}
        Uppercase_code = {keytable[i].upper(): self.alphabet[i].upper() for i in range(len(self.alphabet))}
        self._decode = dict(Lowercase_code)
        self._decode.update(Uppercase_code)

    def encode(self, line):
        if len(line) == 1:
            return self._encode[line] if line in self._encode else line
        else:
            return ''.join([self.encode(char) for char in line])

    def decode(self, line):
        if len(line) == 1:
            return self._decode[line] if line in self._decode else line
        else:
            return ''.join([self.decode(char) for char in line])

frq = 'егпжонщюэбэчмяхыцилдшарсйзвьёктф'
key = 'шифрвженатакдльйоячёспгмзыхбцэую'

cipher = Monoalphabet(key)
line = input()
while line:
    print(cipher.encode(line))
    print()
    line = input()