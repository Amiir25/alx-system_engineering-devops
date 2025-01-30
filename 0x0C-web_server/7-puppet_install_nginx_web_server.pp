#!/usr/bin/enc bash
# Puppet script to install Nginx web server

# Install the Nginx package
package { 'nginx':
  ensure => installed,
}

# Ensure Nginx service is running and enabled
service { 'nginx':
  ensure     => running,
  enable     => true,
  require    => Package['nginx'],
}

# Create the Nginx configuration file
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => '
server {
    listen 80 default_server;
    listen [::]:80 default_server;

    server_name _;

    root /var/www/html;
    index index.html index.htm;

    location / {
        return 200 "Hello World!";
    }

    location /redirect_me {
        return 301 http://$host/;
    }
}
',
  require => Package['nginx'],
  notify  => Service['nginx'],
}

# Ensure the configuration directory exists
file { '/var/www/html':
  ensure => directory,
  require => Package['nginx'],
}

# Ensure the index.html file exists and contains "Hello World!"
file { '/var/www/html/index.html':
  ensure  => file,
  content => 'Hello World!',
  require => File['/var/www/html'],
}

