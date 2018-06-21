#!/bin/bash
#demonstrate variable scope2
#Let's verify their current value

echo $0 :: var1 : $var1, var2: $var2

#Let's change their values

var1=flop
var2=bleuh
export var1
./end.sh

