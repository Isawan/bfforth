The memory layout is to start in this form
 0x00   0x01   0x02   0x03   0x04   0x05   0x06   0x07   0x08   0x09
(0x01) ($N0 ) (0x01) ($N1 ) (0x01) ($M0 ) (0x01) ($M1 ) (0x00) (0x00)
                             ^
We would like to implement a push multiply on the stack leaving
 0x00   0x01   0x02   0x03   0x04   0x05
(0x01) ($L0 ) (0x01) ($L1 ) (0x00) (0x00) 
 ^
Here we will add the two 16 bit big endian numbers L = N * M


It can be shown that the multiplication has the following form
($N0 * $M1 plus $N1 * $M0)*2^8 plus $N1 * $M1
We see here that $L0 = $N0 * $M1 plus $N1 * $M0
                 $L1 = $N1 * $M1
So we will implement three multiplications
The first two is relatively straight forward as we can ignore the carry
A multiplication requires two empty temp cell each
To begin we set 0x04 0x06 to zero
leave the cursor at 0x01
[-]>>[-]<<<<<

Evaluate $N0 = $N0 * $M1
[>>>+<<<-]                                  add  0x01 to 0x04
>>>[                                        move 0x04
  >>>[<<< <<< + >>>>> + > -]                add  0x07 to 0x01 and 0x06
  <[>+<-]                                   add  0x06 to 0x07
<<-]                                        decr 0x04

Evaluate $M0 =  $N1 * $M0
>                                           move 0x05
[->+<]                                      add  0x05 to 0x06
>[                                          move 0x06
  <<<[>>+<+<-]                              add  0x03 to 0x04 and 0x05
  >[<+>-]                                   add  0x04 to 0x03
>>-]                                        decr 0x06

Add $M0 to $N0
<[-<<<<+>>>>]

We need to be careful here as we cannot ignore the carry
This will be slightly more difficult to implement
So let us remind ourselves of the current memory layout
 0x00   0x01   0x02   0x03   0x04   0x05   0x06   0x07   0x08   0x09
(0x01) (0xL1) (0x01) (0x2N) (0x00) (0x00) (0x00) (0x2M) (0x00) (0x00)
                                    ^
Evaluate $N1 * $M1
<<                                          move 0x03
[>>>+<<<-]                                  add  0x03 to 0x06
>>>[                                        move 0x06
  >[<<<<+                                   promise this works

    >+<
    [>-]>[<
      <<+>>
    >->]<<

  >>>>>+<-]
  >[<+>-]
<<-]
<<<<<<
