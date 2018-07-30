MAGIC_STR = "\x00asm"
VERSION_STR = "\x01\x00\x00\x00"

def Module(*args):
    data = ''
    for e in args:
        data += e
    return MAGIC_STR + VERSION_STR + data;
