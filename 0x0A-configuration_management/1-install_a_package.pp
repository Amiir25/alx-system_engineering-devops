# Installs Flask version 2.1.0 from pip3

# Ensure python3 is installed
package { 'python3':
    ensure => installed,
}

# Ensure pip3 is installed
package { 'python3-pip':
    ensure  => installed,
    require => Package['python3'],
}

# Install Flask
exec { 'install-flask':
    command => '/usr/bin/pip3 install Flask==2.1.0',
    path    => ['/usr/bin', '/bin', '/usr/sbin', '/sbin'],
    require => Package['python3-pip'],
    unless  => '/usr/bin/pip3 show Flask | grep -q "Version: 2.1.0"',
}
