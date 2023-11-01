#!/usr/bin/env ruby
#script to parse log file

puts ARGV[0].scan(/\[(?:from:|to:|flags:)(.*?)\]/).join(",")
