from section import ArraySection
from utils import varuint
from const import *

def ExportSection(params):
    return ArraySection(SECTION_EXPORT, params);

def ExportEntry(kind, field, idx):
    return varuint(len(field)) + field + varuint(kind) + varuint(idx)
