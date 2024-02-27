#!/usr/bin/env ruby
#This script:
#   outputs sender phone number or name
#   outputs receiver phone number or name
#   outputs flags that were used
puts ARGV[0].scan(/\[from:(.*?)\] \[to:(.*?)\] \[flags:(.*?)\]/).join(",")
