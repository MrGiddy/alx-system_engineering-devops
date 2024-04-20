# Puppet code to kill a process named killmenow

exec {'terminate_killmenow':
  command => 'pkill killmenow',
  path    => ['/bin', '/usr/bin', '/sbin', '/usr/sbin'],
}
