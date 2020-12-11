import io
import os
import sys

rom = sys.argv[1]
invaders = open(rom,"rb")
size = os.path.getsize(rom)
pointer = 0

while pointer<size:
    opcode = invaders.read(1)
    if opcode == b'\x00':
        print(f'{opcode.hex()}  NOP')
    
    elif opcode == b'\xc3' :
        L = invaders.read(1).hex()
        H = invaders.read(1).hex()
        print(f'{opcode.hex()}  JMP   ${H}{L}')
    
    elif opcode == b'\xc5':
        print(f'{opcode.hex()}  PUSH  B')
    
    elif opcode == b'\xd5':
        print(f'{opcode.hex()}  PUSH  D')
    
    elif opcode == b'\xf5':
        print(f'{opcode.hex()}  PUSH  PSW')
    
    elif opcode == b'\x3e':
        print(f'{opcode.hex()}  MVI   A,#${invaders.read(1).hex()}')
    
    elif opcode == b'\xe5':
        print(f'{opcode.hex()}  PUSH  H')
    
    elif opcode == b'\x32':
        L = invaders.read(1).hex()
        H = invaders.read(1).hex()
        print(f'{opcode.hex()}  STA   ${H}{L}')
    
    elif opcode == b'\x06':
        print(f'{opcode.hex()}  MVI   B,#${invaders.read(1).hex()}')
    
    elif opcode == b'\x0e':
        print(f'{opcode.hex()}  MVI   C,#${invaders.read(1).hex()}')
    
    elif opcode == b'\x16':
        print(f'{opcode.hex()}  MVI   D,#${invaders.read(1).hex()}')
    
    elif opcode == b'\x1e':
        print(f'{opcode.hex()}  MVI   E,#${invaders.read(1).hex()}')

    elif opcode == b'\x26':
        print(f'{opcode.hex()}  MVI   C,#${invaders.read(1).hex()}')
    
    elif opcode == b'\x0f':
        print(f'{opcode.hex()}  RRC')
    
    elif opcode == b'\x03':
        print(f'{opcode.hex()}  INX   B')

    elif opcode == b'\x13':
        print(f'{opcode.hex()}  INX   D')

    elif opcode == b'\x23':
        print(f'{opcode.hex()}  INX   H')

    elif opcode == b'\x33':
        print(f'{opcode.hex()}  INX   SP')
    
    elif opcode == b'\x04':
        print(f'{opcode.hex()}  INR   B')

    elif opcode == b'\x0c':
        print(f'{opcode.hex()}  INR   C')

    elif opcode == b'\x14':
        print(f'{opcode.hex()}  INR   D')

    elif opcode == b'\x1c':
        print(f'{opcode.hex()}  INR   E')
    
    elif opcode == b'\x24':
        print(f'{opcode.hex()}  INR   H')

    elif opcode == b'\x2c':
        print(f'{opcode.hex()}  INR   L')

    elif opcode == b'\x34':
        print(f'{opcode.hex()}  INR   M')

    elif opcode == b'\x3c':
        print(f'{opcode.hex()}  INR   A')

    elif opcode == b'\xda' :
        L = invaders.read(1).hex()
        H = invaders.read(1).hex()
        print(f'{opcode.hex()}  JC   ${H}{L}')

    elif opcode == b'\xd2' :
        L = invaders.read(1).hex()
        H = invaders.read(1).hex()
        print(f'{opcode.hex()}  JNC   ${H}{L}')

    elif opcode == b'\xc2' :
        L = invaders.read(1).hex()
        H = invaders.read(1).hex()
        print(f'{opcode.hex()}  JNZ   ${H}{L}')

    elif opcode == b'\xfa' :
        L = invaders.read(1).hex()
        H = invaders.read(1).hex()
        print(f'{opcode.hex()}  JM   ${H}{L}')

    elif opcode == b'\xf2' :
        L = invaders.read(1).hex()
        H = invaders.read(1).hex()
        print(f'{opcode.hex()}  JP    ${H}{L}')
    
    elif opcode == b'\xe2' :
        L = invaders.read(1).hex()
        H = invaders.read(1).hex()
        print(f'{opcode.hex()}  JPO   ${H}{L}')

    elif opcode == b'\xcd' :
        L = invaders.read(1).hex()
        H = invaders.read(1).hex()
        print(f'{opcode.hex()}  CALL  ${H}{L}')

    elif opcode == b'\x3a' :
        L = invaders.read(1).hex()
        H = invaders.read(1).hex()
        print(f'{opcode.hex()}  LDA   ${H}{L}')

    elif opcode == b'\x1a' :
        print(f'{opcode.hex()}  LDAX  D')
    
    elif opcode == b'\x0a' :
        print(f'{opcode.hex()}  LDAX  B')

    elif opcode == b'\x80' :
        print(f'{opcode.hex()}  ADD   B')

    elif opcode == b'\x81' :
        print(f'{opcode.hex()}  ADD   C')

    elif opcode == b'\x82' :
        print(f'{opcode.hex()}  ADD   D')

    elif opcode == b'\x83' :
        print(f'{opcode.hex()}  ADD   E')

    elif opcode == b'\x84' :
        print(f'{opcode.hex()}  ADD   H')

    elif opcode == b'\x85' :
        print(f'{opcode.hex()}  ADD   L')
    
    elif opcode == b'\xdc' :
        L = invaders.read(1).hex()
        H = invaders.read(1).hex()
        print(f'{opcode.hex()}  CC   ${H}{L}')
    
    pointer+=1