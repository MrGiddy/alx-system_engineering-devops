#!/usr/bin/env bash
# Install and configure nginx web server

exec { 'apt-update':
  command => 'apt update',
  path    => '/usr/bin/'
}

package {'nginx':
  ensure          => installed,
  install_options => ['-y'],
}

file {'404_page':
  ensure  => file,
  path    => '/var/www/html/custom_404.html',
  content => "Ceci n'est pas une page\n\n",
}

file {'dflt_server_block':
  ensure  => file,
  path    => '/etc/nginx/sites-available/default',
  content =>
  'server {
    listen 80 default_server;
    listen [::]:80 default_server;

    root /var/www/html;
    index index.nginx-debian.html;

    location / {
        return 200 "Hello World!\n";
    }

    location /redirect_me {
        return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
    }

    error_page 404 /custom_404.html;
    location = /custom_404.html {
        root /var/www/html;
        internal;
    }
}',
}

service {'nginx':
  ensure    => 'running',
  enable    => true,
}
