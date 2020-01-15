The memory layout is to start in this form
 0x00   0x01   0x02   0x03   0x04   0x05   0x06   0x07   0x08   0x09
(0x01) ($N0 ) (0x01) ($N1 ) (0x01) ($M0 ) (0x01) ($M1 ) (0x00) (0x00)
                             ^
We would like to implement a push subtraction on the stack leaving
 0x00   0x01   0x02   0x03   0x04   0x05
(0x01) ($L0 ) (0x01) ($L1 ) (0x00) (0x00) 
 ^
Here we will subtract the two 16 bit big endian numbers L = N minus M

Set 0x04 and 0x06 to zero
Then move 0x05 to 0x06
Leave cursor over 0x07
[-]>>[-]<
[->+<]
>>

Our memory now looks like this
 0x00   0x01   0x02   0x03   0x04   0x05   0x06   0x07   0x08   0x09
(0x01) ($N0 ) (0x01) ($N1 ) (0x00) (0x00) ($M0 ) ($M1 ) (0x00) (0x00)
                                                  ^
Next we subtract 0x07 from 0x03
We must decrement 0x01 everytime 0x03 moves *pass* zero
To test this we check for 255 value by incrementing 0x03 before if statement
[-<<<+<-
  +
  [
    if code here
  >-]>[
    else code here
    <<<->> 
  >->]<<
  -
  >>>>
]

Finally we can subtract 0x01 by 0x06
We can ignore the effects of overflow as this just wraps around
<
[-<<<<<->>>>>]
<<<<<<

