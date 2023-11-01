#!/usr/bin/env ruby
#script to match 10 digit phone number without spaces or dashes

puts ARGV[0].scan(/^[0-9]{10}$/).join
