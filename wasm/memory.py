from section import ArraySection
from utils import varuint
from const import *

def MemorySection(params):
    return ArraySection(SECTION_MEMORY, params);

def MemoryEntry(min_units, max_units = 0):
    flags = 0
    if max_units != 0:
        flags = 1
        return varuint(flags) + varuint(min_units) + varuint(max_units)
    return varuint(flags) + varuint(min_units)
