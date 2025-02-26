# This code automates the solution to fix the Apache 500 error using strace.

# Ensure correct ownership and permissions
file { '/var/www/html':
  ensure  => directory,
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0755',
  recurse => true,
}

# Ensure Apache is installed
package { 'apache2':
  ensure => installed,
}

# Ensure required modules are enabled
exec { 'enable_php_module':
  command => '/usr/sbin/a2enmod php',
  unless  => '/bin/ls /etc/apache2/mods-enabled/php*',
  notify  => Service['apache2'],
}

# Ensure Apache service is running and enabled
service { 'apache2':
  ensure  => running,
  enable  => true,
  require => Package['apache2'],
}
