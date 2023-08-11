if __name__ == '__main__':
    file_name = './resources/transformation_enc'
    with open(file_name, 'r') as f:
        encoded_flag = f.read()
        flag = []
        for token in encoded_flag:
            second = ord(token) % (1 << 8)
            first = ord(token) // (1 << 8)
            flag.append(chr(first))
            flag.append(chr(second))
        print(''.join(flag))
