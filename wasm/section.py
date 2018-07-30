from utils import varuint

def Section(_id, payload):
    return varuint(_id) + varuint(len(payload)) + payload

def ArraySection(_id, args):
    data = ''
    for e in args:
        data += e
    return Section(_id, varuint(len(args)) + data)

