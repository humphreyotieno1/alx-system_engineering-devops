#!/usr/bin/env bash
# Connecting without a password

include stdlib

file_line { 'Turn off passwd auth':
  ensure  => present,
  path	  => '/etc/ssh/ssh_config',
  line	  => 'PasswordAuthentication no',
  match	  => '^#PasswordAuthentication',
}

file_line { 'Declare identity file':
  ensure  => present,
  path	  => '/etc/ssh/ssh_config',
  line	  => 'IdentifyFile ~/.ssh/school',
  match	  => '^IdentifyFile',
}
