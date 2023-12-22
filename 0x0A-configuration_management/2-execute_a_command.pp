# Using puppet to create a manifest to kill a process called killmenow
# Uses exec and pkill

exec { 'pkill killmenow':
  command => '/usr/bin/pkill -f /killmenow',
}
