from section import ArraySection
from utils import varuint
from const import *

def CodeSection(params):
    return ArraySection(SECTION_CODE, params);

def CodeEntry(locals_, body):
    l = varuint(len(locals_.keys()))
    for k in locals_.keys():
        l += varuint(locals_[k])
        l += varuint(k)
    return varuint(len(l) + len(body) + 1) + l + body + '\x0b'
