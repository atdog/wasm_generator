from section import ArraySection
from utils import varuint
from const import *

def DataSection(params):
    return ArraySection(SECTION_DATA, params);

def DataEntry(idx, expr, data):
    return varuint(idx) + expr + varuint(len(data)) + data
