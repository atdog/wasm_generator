from utils import varuint
from const import *

def UserSection(name, payload):
    section_data = varuint(len(name)) + name + payload
    return varuint(SECTION_USER) + varuint(len(section_data)) + section_data
