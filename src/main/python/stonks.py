encoded_flag = '0x9a373d00x804b0000x80489c30xf7f7ad800xffffffff0x10x9a351600xf7f881100xf7f7adc7(nil)0x9a361800x50x9a373b00x9a373d00x6f6369700x7b4654430x306c5f490x345f74350x6d5f6c6c0x306d5f790x5f79336e0x353430360x643036640xff8f007d0xf7fb5af80xf7f884400x323e2e000x1(nil)0xf7e17ce90xf7f890c00xf7f7a5c00xf7f7a0000xff8fc3780xf7e0868d0xf7f7a5c00x8048eca0xff8fc384(nil)0xf7f9cf09'
hex_string = []
for section in encoded_flag.split('(nil)'):
    for token in section.split('0x'):
        if not token:
            continue

        if len(token) != 8:
            continue

        hex_string.append(token)

# hex_string.reverse()
flag = []

for token in hex_string:
    byte_arr = bytes.fromhex(token)
    byte_arr = byte_arr[::-1]
    for character in byte_arr:
        flag.append(chr(character))

print(''.join(flag))
