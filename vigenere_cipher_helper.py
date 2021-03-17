"""
Vigenère Cipher Helper

link: https://www.codewars.com/kata/52d1bd3694d26f8d6e0000d3

The Vigenère cipher is a classic cipher originally developed by Italian 
cryptographer Giovan Battista Bellaso and published in 1553. 
It is named after a later French cryptographer Blaise de Vigenère, 
who had developed a stronger autokey cipher 
(a cipher that incorporates the message of the text into the key).

The cipher is easy to understand and implement, 
but survived three centuries of attempts to break it, 
earning it the nickname "le chiffre indéchiffrable" or "the indecipherable cipher."

From Wikipedia:

The Vigenère cipher is a method of encrypting alphabetic text by 
using a series of different Caesar ciphers based on the letters of a keyword. 
It is a simple form of polyalphabetic substitution.

. . .

In a Caesar cipher, each letter of the alphabet is shifted along some number of places; 
for example, in a Caesar cipher of shift 3, A would become D, 
B would become E, Y would become B and so on. 
The Vigenère cipher consists of several Caesar ciphers in sequence with different shift values.

Assume the key is repeated for the length of the text, character by character. 
Note that some implementations repeat the key over characters only 
if they are part of the alphabet -- this is not the case here.

The shift is derived by applying a Caesar shift to a character 
with the corresponding index of the key in the alphabet.

Visual representation:

"my secret code i want to secure"  // message
"passwordpasswordpasswordpasswor"  // key
Write a class that, when given a key and an alphabet, can be used to encode and decode from the cipher.

Example
var alphabet = 'abcdefghijklmnopqrstuvwxyz';
var key = 'password';

// creates a cipher helper with each letter substituted
// by the corresponding character in the key
var c = new VigenèreCipher(key, alphabet);

c.encode('codewars'); // returns 'rovwsoiv'
c.decode('laxxhsj');  // returns 'waffles'
Any character not in the alphabet must be left as is. For example (following from above):

c.encode('CODEWARS'); // returns 'CODEWARS'
"""


class VigenereCipher(object):
    def __init__(self, key, alphabet):
        self.key = key
        self.alphabet = alphabet
        self.movement = tuple(ord(i) - ord('a') for i in key)

    def get_enc_symb(self, symb, code_symb):
        if symb in self.alphabet:
            movement = self.alphabet.index(code_symb) - self.alphabet.index(self.alphabet[0])

            return self.alphabet[(self.alphabet.index(symb) + movement) %
                                 len(self.alphabet)]
        else:
            return symb

    def get_dec_symb(self, symb, code_symb):
        if symb in self.alphabet:
            movement = self.alphabet.index(code_symb) - self.alphabet.index(self.alphabet[0])

            return self.alphabet[(self.alphabet.index(symb) - movement) %
                                 len(self.alphabet)]
        else:
            return symb

    def encode(self, text):
        answer = ""
        counter = 0
        for i in text:
            if i in alphabet:
                answer += self.get_enc_symb(i, self.key[counter])
                counter = (counter + 1) % len(self.movement)
            else:
                answer += i
                counter = (counter + 1) % len(self.movement)
        return answer

    def decode(self, text):
        answer = ""
        counter = 0
        for i in text:
            if i in alphabet:
                answer += self.get_dec_symb(i, self.key[counter])
                counter = (counter + 1) % len(self.movement)
            else:
                answer += i
                counter = (counter + 1) % len(self.movement)
        return answer


def main():
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    key = 'password'

    # creates a cipher helper with each letter substituted
    # by the corresponding character in the key
    c = VigenereCipher(key, alphabet)
    print(list(c.movement))

    print(c.encode('codewars'))  # returns 'rovwsoiv'
    print(c.decode('laxxhsj'))  # returns 'waffles'


if __name__ == "__main__":
    main()
