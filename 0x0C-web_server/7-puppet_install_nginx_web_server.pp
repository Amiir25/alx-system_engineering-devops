class nginx_setup {
    package { 'nginx':
        ensure => installed,
    }

    service { 'nginx':
        ensure    => running,
        enable    => true,
        require   => Package['nginx'],
    }

    file { '/var/www/html/index.html':
        ensure  => file,
        content => '<html><body><h1>Hello World!</h1></body></html>',
        require => Package['nginx'],
    }

    file { '/etc/nginx/sites-available/default':
        ensure  => file,
        content => "
server {
    listen 80;
    root /var/www/html;
    index index.html;

    location / {
        try_files \$uri \$uri/ =404;
    }

    location /redirect_me {
        return 301 http://example.com;
    }
}",
        require => Package['nginx'],
        notify  => Service['nginx'],
    }
}
