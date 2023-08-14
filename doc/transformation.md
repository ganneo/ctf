#Transformation Writeup

I wonder what this really is... [enc](https://mercury.picoctf.net/static/1d8a5a2779c4dc24999f0358d7a1a786/enc) \
`''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])`

Downloading and opening the enc file we see "灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸彥㜰㍢㐸㙽". The name of the file is enc so this is
probably the encrypted flag. Looking back at the problem, we can see a little code snippet. The variable name that was
used was flag, so it most likely would be how the flag was encrypted. To reverse what they did to encrypt the flag, we
need to first understand what is being done. We can break the code up into 3 parts.
1. `''.join([ ])`
2. `chr( ) for i in range(0, len(flag), 2)`
3. `ord(flag[i] << 8) + ord(flag[i + 1])`

The first part is formatting the answer so that there are no spaces in the encrypted flag. The second part is iterating
through all the values in the flag by increments of 2. In the third part we can finally see the encrypting action.
Notice that the third part uses the index of `i` and `i + 1` which is why the flag was iterated using 2 values not 1.
The `ord()` function converts a string to its corresponding ascii2 value. The first `ord()` encloses the expression
`flag[i] << 8`. `<< 8` increases the ascii value by 2^8. So the third part is the first ascii value + 256 + the second
ascii value.

Since ascii values do not exceed 256, we can separate the sums by using quotients and remainders. Taking the mod of 256
will result in the second and smaller number and using floor division we can get the first number.

Running the code we see the flag outputted in the terminal: picoCTF{16_bits_inst34d_of_8_e703b486}