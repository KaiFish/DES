from Bits import *
from Input import Input

assert ones(1) == 0b1
assert ones(2) == 0b11
assert ones(3) == 0b111
assert ones(64) == 2**64-1

assert Input.chunk("hello world") == ['01101000', '01100101', '01101100', '01101100', '01101111', '00100000', '01110111', '01101111', '01110010', '01101100', '01100100']

assert Input.sanitize("abcdefgh") == '0110000101100010011000110110010001100101011001100110011101101000'

assert leftRotate('1101011') == '1010111'

print("tests pass :tada:")
