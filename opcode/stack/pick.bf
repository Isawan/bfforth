The memory layout is to start in this form
 0x00   0x01   0x02   0x03   0x04   0x05   0x06   0x07   0x10   0x11   0x12   0x13
(0x01) (0x0N) (0x01) (0x1N) (0x01) (0x0M) (0x01) (0x1M) (0x01) (0x0U) (0x01) (0x1U)
                                                         ^
First clear 0x10 0x12 we need this to mark the top of the array
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
    +<< <<[-]>> [>>] <       remember 0x10 is non zero here

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