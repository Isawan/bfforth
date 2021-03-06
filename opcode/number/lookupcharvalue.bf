The goal of this script is to find the first index of a char in a given array
This allows conversion of a string into the number with the array used to
decode the base

The layout is given
0x00 to 0x03 is the output position; it also holds previous digit value
0x04 to 0x07 and 0x08 to 0x0B is the decimal place multiplier
0x10 to 0x13 is the char to be decoded
0x14 onwards is the char array where index gives decoding value

 0x00   0x01   0x02   0x03   0x04   0x05   0x06   0x07 
(0x01) ($V0 ) (0x01) ($V1 ) (0x01) ($X0 ) (0x01) ($X1 )
                             
 0x08   0x09   0x0A   0x1B   0x0C   0x0D   0x0E   0x0F 
(0x01) ($X0 ) (0x01) ($X1 ) (0x01) ($Y0 ) (0x01) ($Y1 )
 
 0x10   0x11   0x12   0x13   0x14   0x15   0x16   0x17 
(0x01) (0x00) (0x01) ($Z  ) (0x00) (0x00) (0x00) (0x30)
 ^
 0x18   0x19   0x1A   0x1B   0x1C   0x1D   0x1E   0x1F 
(0x00) (0x00) (0x00) (0x31) (0x00) (0x00) (0x00) (0x32)  and so on

Start by zeroing out 0x0E 0x10 and 0x12
<<[-]>>[-]>>[-]

Copy 0x13 to 0x10 ending at 0x12 
>[-<+<<+>>>]<[->+<]+

start a loop
[
  for ease of explanation we look at the case where index starts at 0x12
  [-]                            zero out 0x12
  go to 0x17 setting 0x15 to zero as we pass 
  >>>[-]>>                       go to 0x17 set 0x15 to zero as we pass
  [-<+<+>>]<<[->>+<<]            copy 0x17 to 0x16 finish at 0x15
  <<<<<                          go to 0x10
  [->>>>+>>-<<<<<<]              sub value 0x2Z at index 0x10 from 0x16
                                 also set 0x14 to 0x2Z
                                 if 0x16 holds 0 then cell 0x13 == cell 0x17
				 end at 0x10
  >[->>>>+<<<<]                  move 0x11 to 0x15
  >>>>+                          increment 0x15
  now leave a trail of 1s to follow back
  <<<+<<+>>>>>                  set 0x10 0x12 to 1
  >
]
remove original decode char
<<<<[<<]>>>>>[-]<[>>]
copy back
< [-<<<[<<]>>>>>+<[>>]<]
clean up
<[-]<<[-<<]>>+>>+<<
