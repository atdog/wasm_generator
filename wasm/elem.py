from section import ArraySection
from utils import varuint
from const import *

def ElemSection(params):
    return ArraySection(SECTION_ELEMENT, params);

def ElemEntry(idx, expr, indices):
    elems = ''
    for indice in indices:
        elems += chr(indice)
    return varuint(idx) + expr + varuint(len(indices)) + elems
