# Solution 9: Bytecode Relay

A compact emulator is safer than trying to execute an unknown artifact as native code. The image is only data, and the implementation below supports exactly the six documented opcodes.

```python
from pathlib import Path

image = bytes.fromhex(
    Path("challenges/hard/09-bytecode-relay/program.hex").read_text()
)

if image[:4] != b"CTV1":
    raise ValueError("Bad image magic")

pc = 4
registers = [0, 0, 0, 0]
output = bytearray()


def take(count):
    global pc
    if pc + count > len(image):
        raise ValueError("Truncated instruction")
    values = image[pc : pc + count]
    pc += count
    return values


def check_register(index):
    if index >= len(registers):
        raise ValueError(f"Invalid register r{index}")


while True:
    opcode = take(1)[0]

    if opcode == 0x10:  # MOVI
        register, immediate = take(2)
        check_register(register)
        registers[register] = immediate

    elif opcode == 0x20:  # XOR
        destination, source = take(2)
        check_register(destination)
        check_register(source)
        registers[destination] ^= registers[source]

    elif opcode == 0x21:  # SUB
        destination, source = take(2)
        check_register(destination)
        check_register(source)
        registers[destination] = (
            registers[destination] - registers[source]
        ) & 0xFF

    elif opcode == 0x30:  # ROR
        register, bits = take(2)
        check_register(register)
        bits %= 8
        value = registers[register]
        if bits:
            value = ((value >> bits) | (value << (8 - bits))) & 0xFF
        registers[register] = value

    elif opcode == 0x40:  # OUT
        register = take(1)[0]
        check_register(register)
        output.append(registers[register])

    elif opcode == 0xFF:  # HALT
        break

    else:
        raise ValueError(f"Unknown opcode 0x{opcode:02x} at {pc - 1}")

print(output.decode("utf-8"))
```

The emitted output is:

```text
flag{bytecode_emulation_beats_guessing}
```

## What the program does

For each output byte, the image loads an encoded value and two changing constants, applies XOR and subtraction, rotates the result right, then emits it. The repeated instruction pattern is visible after a few decoded instructions, but full emulation avoids manual arithmetic mistakes.

## Defensive lesson

Treat unknown bytecode as untrusted input. Use a strict opcode allowlist, validate every operand and boundary, limit instruction count for programs with branches, and expose no host capabilities unless the format genuinely requires them.
