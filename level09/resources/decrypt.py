import sys

def decrypt(data: bytes) -> bytes:
    result = bytearray()

    for i, b in enumerate(data):
        if b != 10:
            result.append((b - i) % 256)

    return bytes(result)

def is_ascii(data: bytes) -> bool:
    return all(b < 128 for b in data)

if len(sys.argv) < 2:
    print(sys.argv[0] + " <file>")
    sys.exit(1)

with open(sys.argv[1], "rb") as f:
    data = f.read()

decrypted = decrypt(data)

if is_ascii(decrypted):
    text = decrypted.decode("ascii")
    print(text)
else:
    print("Not All Bytes are decodable to ASCII")
