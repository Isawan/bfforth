Here we setup the stack for the rpn machine
Each element on our stack is implemented by an array with elements:
(1 0) for empty element
(0 n) for occupied element where n is the stored number
To simplify implementation we include a first element (0 0) at the base


begin by setting cell to 255 leave one zero to signify start of array
>>-
next we move this value over; reduce by one; and leave a one in previous spot;
repeat
the effect is to produce an array with 254 elements with elements (1 0)
[[->>+<<]+>>-]

we have now setup the stack
we chose (1 0) for empty spots as it allows us to easily move back to the start
of the stack by hopping off the ones
Example:
to move to the top of the stack we do this
<<[<<]
and to move back
>>[>>]




