# kill a process
exec { 'killmenow':
  command => '/bin/pkill killmenow',
}
