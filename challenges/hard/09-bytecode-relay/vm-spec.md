# CTF-VM/1 specification

## Image format

The decoded byte image begins with the ASCII magic value `CTV1`. Execution starts at byte offset 4.

The machine has four 8-bit registers named `r0` through `r3`. All registers begin at zero. Arithmetic wraps modulo 256. Operands are unsigned bytes.

## Instructions

| Opcode | Encoding | Meaning |
|---|---|---|
| `0x10` | `10 reg imm` | `MOVI`: set `reg` to immediate byte `imm` |
| `0x20` | `20 dst src` | `XOR`: set `dst = dst XOR src` |
| `0x21` | `21 dst src` | `SUB`: set `dst = (dst - src) mod 256` |
| `0x30` | `30 reg bits` | `ROR`: rotate `reg` right by `bits mod 8` |
| `0x40` | `40 reg` | `OUT`: append the current byte in `reg` to output |
| `0xFF` | `ff` | `HALT`: stop execution |

A register operand outside `0..3`, an unknown opcode, a truncated instruction, or execution beyond the image is invalid.

Interpret the collected output bytes as UTF-8 after the program halts.
