__author__ = 'Timofey Khirianov'
# -*- coding: utf8 -*-

class Vigenere:
    alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

    def __init__(self, keyword):
        self.alphaindex = {self.alphabet[index]: index for index in range(len(self.alphabet))}
        self.key = [self.alphaindex[letter] for letter in keyword.lower()]

    def caesar(self, letter, shift):
        if letter in self.alphaindex:  # шбжцлюэи ьтчоэ
            index = (self.alphaindex[letter] + shift) % len(self.alphabet)
            cipherletter = self.alphabet[index]
        elif letter.lower() in self.alphaindex:  # йэряэоюэи ьтчоэ
            cipherletter = self.caesar(letter.lower(), shift).upper()
        else:
            cipherletter = letter
        return cipherletter

    def encode(self, line, key=None):
        if not key:
            key = self.key
        ciphertext = []
        i = 0
        for letter in line:
            shift = key[i]
            cipherletter = self.caesar(letter, shift)
            ciphertext.append(cipherletter)
            i = (i + 1) % len(key)
    def minicaesar(self, letter, shift):
        if letter in self.alphaindex:  # шбжцлюэи ьтчоэ
            index = (self.alphaindex[letter] - shift) % len(self.alphabet)
            item = self.alphabet[index]
        elif letter.lower() in self.alphaindex:  # йэряэоюэи ьтчоэ
            item = self.minicaesar(letter.lower(), shift).upper()
        else:
            item = letter
        return item


    def decode(self, line):
        laner = []
        cnt = 0
        for i in line:
            shift = self.key[cnt]
            item = self.minicaesar(i, shift)
            laner.append(item)
            cnt = (cnt + 1) % len(self.key)
        return ''.join(laner)


keyword = 'столлман'
cipher = Vigenere(keyword)
line = input()
while line != '.':
    print(cipher.decode(line))
    line = input()