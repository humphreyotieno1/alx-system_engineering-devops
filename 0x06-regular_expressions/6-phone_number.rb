#!/usr/bin/env ruby
#script to match 10 digit phone number without spaces or dashes

puts ARGV[0].scan(/^d{10,10}$/).join
