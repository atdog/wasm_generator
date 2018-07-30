from section import ArraySection
from utils import varuint
from const import *

def GlobalSection(params):
    return ArraySection(SECTION_GLOBAL, params);

def GlobalEntry(type_, mutable, expr):
    return varuint(type_) + varuint(mutable) + expr
