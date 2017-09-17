The memory layout is to start in this form
 0x00   0x01   0x02   0x03   0x04   0x05   0x06   0x07   0x10   0x11
(0x01) (0x1N) (0x01) (0x2N) (0x01) (0x1M) (0x01) (0x2M) (0x00) (0x00)
                             ^
We would like to implement a push multiply on the stack leaving
 0x00   0x01   0x02   0x03   0x04   0x05
(0x01) (0x1L) (0x01) (0x2L) (0x00) (0x00) 
 ^
Here we will add the two 16 bit big endian numbers L = N * M


It can be shown that the multiplication has the following form
(N1 * M2 plus N2 * M1)*2^8 plus N2 * M2
We see here that L1 = N1 * M2 plus N2 * M1
                 L2 = N2 * M2
So we will implement three multiplications
The first two is relatively straight forward as we can ignore the carry
A multiplication requires two empty temp cell each
To begin we set 0x04 0x06 to zero
leave the cursor at 0x01
[-]>>[-]<<<<<

Evaluate N1 = N1 * M2
[>>>+<<<-]                                  add  0x01 to 0x04
>>>[                                        move 0x04
  >>>[<<< <<< + >>>>> + > -]                add  0x07 to 0x01 and 0x06
  <[>+<-]                                   add  0x06 to 0x07
<<-]                                        decr 0x04

Evaluate M1 =  N2 * M1
>                                           move 0x05
[->+<]                                      add  0x05 to 0x06
>[                                          move 0x06
  <<<[>>+<+<-]                              add  0x03 to 0x04 and 0x05
  >[<+>-]                                   add  0x04 to 0x03
>>-]                                        decr 0x06

Add M1 to N1
<[-<<<<+>>>>]

We need to be careful here as we cannot ignore the carry
This will be slightly more difficult to implement
So let us remind ourselves of the current memory layout
 0x00   0x01   0x02   0x03   0x04   0x05   0x06   0x07   0x10   0x11
(0x01) (0xL1) (0x01) (0x2N) (0x00) (0x00) (0x00) (0x2M) (0x00) (0x00)
                                    ^
Evaluate N2 * M2
<<                                          move 0x03
[>>>+<<<-]                                  add  0x03 to 0x06
>>>[                                        move 0x06
  >[<<<<+

    >+<
    [>-]>[<
      <<+>>
    >->]<<

  >>>>>+<-]
  >[<+>-]
<<-]
<<<<<<
