#!/usr/bin/env bash
# Connecting without a password

file { '/etc/ssh/ssh_config':
  ensure  => present,
  content => "
  	  #ssh client configuration
	  host*
	  IdentityFile ~/.ssh/school
	  PasswordAuthentication no
	  ",
}
