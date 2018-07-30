from section import ArraySection
from utils import varuint
from const import *

def ImportSection(params):
    return ArraySection(SECTION_IMPORT, params);

def ImportEntry(module, field, kind, ext):
    return varuint(len(module)) + module + varuint(len(field)) + field + varuint(kind) + varuint(ext)
