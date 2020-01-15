The memory layout is to start in this form
 0x00   0x01   0x02   0x03   0x04   0x05   0x06   0x07   0x08   0x09
(0x01) ($N0 ) (0x01) ($N1 ) (0x01) ($M0 ) (0x01) ($M1 ) (0x00) (0x00)
                             ^
We would like to implement a push add on the stack leaving
 0x00   0x01   0x02   0x03   0x04   0x05
(0x01) ($L0 ) (0x01) ($L1 ) (0x00) (0x00) 
 ^
Here we will add the two 16 bit big endian numbers $L = $N plus $M

Begin by positioning over 0x05
>

We now start a loop to reduce 0x05 and increment 0x01
We can ignore the effects of overflow as this just wraps around
[-<<<<+>>>>]

set 0x04 and  0x06 to zero
Move over to 0x07  
<[-]>>[-]>

Our memory now looks like this
 0x00   0x01   0x02   0x03   0x04   0x05   0x06   0x07   0x08   0x09
(0x01) ($Y  ) (0x01) ($N1 ) (0x00) (0x00) (0x00) ($M1 ) (0x00) (0x00)
                                                  ^

Next we add the 0x07 onto 0x03
We will also set 0x04 to 1 each time we move to 0x03
this is for implementing if statement
If 0x03 is zero we increment 0x01 by one ie carry add
[-<<<+<+
  [
  >-]>[
    <<<+>>
  >->]<<
  >>>>
]
<<<<<<<



