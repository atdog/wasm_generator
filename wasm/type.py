from section import ArraySection
from utils import varuint
from const import *

def TypeSection(params):
    return ArraySection(SECTION_TYPE, params);

def TypeEntry(type_, params, rets):
    p = varuint(len(params))
    for param in params:
        p += varuint(param)
    r = varuint(len(rets))
    for ret in rets:
        r += varuint(ret)
    return varuint(type_) + p + r
