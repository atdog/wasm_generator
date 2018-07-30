#!/usr/bin/env python

from pwn import *
from wasm import *

m = Module(
        TypeSection([
            TypeEntry(TYPE_FUNC, (TYPE_i64, TYPE_i64, TYPE_i64), ()), # type index 0
            TypeEntry(TYPE_FUNC, (TYPE_i64, TYPE_i64, TYPE_i64), ()), # type index 1
            TypeEntry(TYPE_FUNC, (TYPE_i64, TYPE_i64, TYPE_i64), ()), # type index 2
            TypeEntry(TYPE_FUNC, (TYPE_i64, TYPE_i64, TYPE_i64), ()), # type index 2
            ]),
        FunctionSection([
            FunctionEntry(0), # function index 0 -> type[0]
            FunctionEntry(1), # function index 1 -> type[1]
            FunctionEntry(1), # function index 2 -> type[1]
            ]),
        TableSection([
            # 1024 is constraint
            TableEntry(TYPE_ANYFUNC, 1024), # memory index 0
            ]),
        MemorySection([
            # 528 is contraint (528 * 64 = 33792K)
            MemoryEntry(528), # memory index 0
            ]),
        ExportSection([
            ExportEntry(KIND_FUNCTION, 'apply', 0), # points to function 0
            ]),
        ElemSection([
            ElemEntry(0, CONST_i32(0), [0, 1, 2]),
            ]),
        CodeSection([
            CodeEntry({TYPE_i32: 2, TYPE_i64: 1}, ''),  # function 0
            CodeEntry({}, ''),                          # function 1
            CodeEntry({TYPE_i32: 2}, ''),               # function 2
            ]),
        DataSection([
            DataEntry(0, CONST_i32(1), 'test string\x00'),
            DataEntry(0, CONST_i32(4), 'empty string\x00'),
            ]),
        )

print enhex(m)

with open('test.wasm', 'w') as fh:
    fh.write(m)
