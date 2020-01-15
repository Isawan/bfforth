The memory layout is to start in this form
 0x00   0x01   0x02   0x03   0x04   0x05   0x06   0x07   0x08   0x09   0x0A   0x0B
(0x01) ($N0 ) (0x01) ($N1 ) (0x01) ($M0 ) (0x01) ($M1 ) (0x01) ($U0 ) (0x01) ($U1 )
                                                         ^
First clear 0x08 0x0A we need this to mark the top of the array
<<[-]>>[-]>>[-]<

Next we need to bridge into the stack
+[
  bridge
  >>[
    < << << [<<]
    +<< <<[-]>>
    [>>] >>>
  -]
  <<-
  
  here we implement the carry 
  <+
  >[
    >>-<<
    we need to run bridge once more 
    this does effectively the same as above
    <[<<]
    +<< <<[-]>> [>>] <       remember 0x08 is non zero here

    <-
    >[>+<-]
  ]
  >[<+>-]
  <<[
  -]>

]

Now perform the copying
First part
<<<[<<]<
[>>> [>>] > + >+<  <<<[<<]<-]
Copy back
>>>[>>]>>
[<<<<[<<]<+>>>[>>]>>-]
Second part
<<<<[<<]>
[>[>>]>>>+ <+ <<<<[<<]>-]
Copy back
>[>>]>>
[<<<<[<<]>+>[>>]>>-]

Clean up and set the ones
<<<<[<<]+[>>]>>+<<+
