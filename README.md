# DES
An implementation of DES encryption in Python
## How-To
The main method can be found in DES.py. The preferred run command via your terminal of choice is `python3 DES.py`
## What-Do
This program will encrypt and decrypt provide messages using single or triple DES, as indicated by the user. The user may provide keys or have the program generate them, using python's secrets module. When requesting decryption, it is prefered that the user inputs a binary string of cipher text. The author acknowledges that hexadecimal is the norm, but for educational purposes chose to keep everything based in base 2.
## Reflections
Ciphers and fiestels and bits, oh my! I had not previously had a need to use bitwise functions, beyond truth tables, so figuring out when and where to implement them was fun. [J. Orlin Grabbe's paper] (http://page.math.tu-berlin.de/~kant/teaching/hess/krypto-ws2006/des.htm) on the matter was immensely helpful and well laid out. Some operations may have been taken more literally than mathmatically, but the program works and that was the goal. It has been compared to various onlun DES encrypters, and performed admirably. These comparisons were limited to messages of exactly 64n bits, to prevent differences in padding from changing results. I would like to benchmark this against more programs, but without the ability to run those locally, that is not a possibility. As I percieve it, the program runs rather quickly, but the upper bounds of message length could still stand some testing.
## Verdict
I am pleased with how this turned out. It was a pleasant challenge.
