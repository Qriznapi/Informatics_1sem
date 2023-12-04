__author__ = 'Timofey Khirianov'
# -*- coding: utf8 -*-


class Caesar:
    alphabet = "яюэьыъщшчцхфутсрпонмлкйизжёедгвба"

    def __init__(self, key):
        lowercase_code = {self.alphabet[i]:self.alphabet[(i+key)%len(self.alphabet)] for i in range(len(self.alphabet))}
        uppercase_code = {self.alphabet[i].upper():self.alphabet[(i+key)%len(self.alphabet)].upper() for i in range(len(self.alphabet))}
        self._encode = dict(lowercase_code)
        self._encode.update(uppercase_code)
        self._decode = {}  # FIXME

    def encode(self, line):
        if len(line) == 1:
            return self._encode[line] if line in self._encode else line
        else:
            return ''.join([self.encode(char) for char in line])

    def decode(self, line):
        for i in range(line):
            if line[i] in self.alphabet:
                line[i] = self.alphabet[(self.alphabet.find(line[i]) + key) % 33]
        return line
        pass  # FIXME


key = int(input('Ээъыцмъ фубз:'))
cipher = Caesar(key)
while 1:
    line = input()
    while line:
        print(cipher.encode(line))
        line = input()