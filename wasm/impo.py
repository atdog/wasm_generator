from section import ArraySection
from utils import varuint
from const import *

def ImportSection(params):
    return ArraySection(SECTION_IMPORT, params);

def ImportEntry(module, field, kind, *ext):
    prefix = varuint(len(module)) + module + varuint(len(field)) + field + varuint(kind)
    payload = ''
    if kind == KIND_FUNCTION:
        payload = varuint(ext[0])
    elif kind == KIND_MEMORY:
        min_units = ext[0]
        flags = 0
        if len(ext) > 1:
            flags = 1
            max_units = ext[1]
            payload = varuint(flags) + varuint(min_units) + varuint(max_units)
        else:
            payload = varuint(flags) + varuint(min_units)
    return prefix + payload
