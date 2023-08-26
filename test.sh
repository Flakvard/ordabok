#!/bin/bash

# add color to test outputs
. ANSIcolor
initializeANSI

function assertEQ
{
  local result="$1"
  local expected="$2"
  local command="$3"
if [[ "${result}" == "${expected}" ]]; then
  echo "${greenb}${whitef}Test Passed!${reset} ${command}"
else
  echo "${redb}${whitef}Test Failed!${reset} ${command}"
fi
}

#########################################################################
######################## ord -e #########################################
#########################################################################
function test_a_option(){
local result=$(ord -e baby)
local expected
local command="ord -e baby"
read -r -d '' expected <<- EOF
<<insert text here>>
EOF
assertEQ "$result" "$expected" "$command"
echo "$result"
echo "$expected"
}
test_a_option
