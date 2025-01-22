# Installs Flask version 2.1.0 from pip3

# Ensure python3 is installed
package { 'python3':
    ensure => installed,
}

# Ensure pip3 is installed
package { 'python3-pip':
    ensure => installed,
}

# Install Flask
package { 'Flask':
    ensure   => '2.1.0',
    provider => 'pip3',
    require  => Package['python3-pip'],
}
