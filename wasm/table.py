from section import ArraySection
from utils import varuint
from const import *

def TableSection(params):
    return ArraySection(SECTION_TABLE, params);

def TableEntry(type_, min_units, max_units = 0):
    flags = 0
    if max_units != 0:
        flags = 1
        return varuint(type_) + varuint(flags) + varuint(min_units) + varuint(max_units)
    return varuint(type_) + varuint(flags) + varuint(min_units)
