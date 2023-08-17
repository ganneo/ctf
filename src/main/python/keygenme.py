import hashlib

key = ''
username_trial = b'ANDERSON'
index_values = [4, 5, 3, 6, 2, 7, 1, 8]

for idx in index_values:
    key += hashlib.sha256(username_trial).hexdigest()[idx]

print(key)
