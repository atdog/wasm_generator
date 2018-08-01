from utils import varuint

def ins_i32_const(imm):
    return '\x41' + varuint(imm)

def ins_i64_const(imm):
    return '\x42' + varuint(imm)

def ins_call(idx):
    return '\x10' + varuint(idx)

def ins_set_global(idx):
    return '\x24' + varuint(idx)

def ins_ret():
    return '\x0f'
