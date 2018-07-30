from section import ArraySection
from utils import varuint
from const import *

def FunctionSection(params):
    return ArraySection(SECTION_FUNCTION, params);

def FunctionEntry(type_idx):
    return varuint(type_idx)
