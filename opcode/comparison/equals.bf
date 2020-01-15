The memory layout is to start in this form
 0x00   0x01   0x02   0x03   0x04   0x05   0x06   0x07   0x08   0x09
(0x01) ($N0 ) (0x01) ($N1 ) (0x01) ($M0 ) (0x01) ($M1 ) (0x00) (0x00)
                             ^
We would like to implement an equality comparison on the stack leaving
 0x00   0x01   0x02   0x03   0x04   0x05
(0x01) (0x00) (0x01) ($L ) (0x00) (0x00) 
 ^
where index 0x03 contains either 0 or 1

we start by checking equality between 0x01 and 0x05
<<<                                    goto 0x01
[->>>>-<<<<]+>>>>[<<<<->>>>[-]]
next check equality between 0x03 and 0x07
<<                                     goto 0x03
[->>>>-<<<<]+>>>>[<<<<->>>>[-]]        end  0x07 
clean up the one trails
<[-]<<[-]<                             end  0x03

apply 0x01 AND 0x03
make 0x03 negative
[
  [-]<<[>>+<<[-]]
][-]<
