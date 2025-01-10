# Executes a command to kill a process

exec { 'kill_killmenow':
    command => '/usr/bin/pkill -f killmenow',
    onlyif  => '/usr/bin/pgrep -f killmenow',
    path    => ['/usr/bin', '/bin'],
}
