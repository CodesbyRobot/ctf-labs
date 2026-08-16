# Challenge 9: Bytecode Relay

A retired training appliance stored its completion message as a program for a tiny virtual machine. The original emulator is gone, but the bytecode image and instruction reference remain.

## Goal

Execute [`program.hex`](program.hex) according to [`vm-spec.md`](vm-spec.md) and recover the emitted flag.

## Approach

1. Remove whitespace from `program.hex` and decode the hexadecimal text to bytes.
2. Validate the four-byte image header.
3. Start the program counter immediately after the header.
4. Implement each instruction with the documented operand widths and 8-bit arithmetic.
5. Collect bytes produced by `OUT` until `HALT`.

Manual disassembly is possible, but a small, defensive emulator is less error-prone.

## Scope

The VM is synthetic and intentionally has no file, process, or network instructions. It can only transform register values and emit bytes.

## Lesson

Reverse engineering becomes safer and more reliable when the execution model is explicit. Validate image structure, reject unknown opcodes, bound the program counter, and keep toy emulation isolated from real system capabilities.
