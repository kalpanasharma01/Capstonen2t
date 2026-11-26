// Box.asm
// K = 72

@18688
D=A
@R0
M=D

@20
D=A
@R1
M=D

(DRAW)

@R0
A=M
M=-1

@R0
D=M
@32
D=D+A
@R0
M=D

@R1
MD=M-1
@DRAW
D;JGT

(END)
@END
0;JMP
