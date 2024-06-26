package { 'nginx':
	ensure => 'present',
	provider => 'apt'
}

file { '/data':
  ensure  => 'directory'
}

file { '/data/web_static':
  ensure => 'directory'
}

file { '/data/web_static/releases':
  ensure => 'directory'
}

file { '/data/web_static/releases/test':
  ensure => 'directory'
}

file { '/data/web_static/shared':
  ensure => 'directory'
}

file { '/data/web_static/releases/test/index.html':
	ensure => 'present',
	content => 'Hello World'
}

exec { 'symbolic_link':
	command => 'ln -sf /data/web_static/releases/test/ /data/web_static/current',
}

exec { 'change_owner':
	command => 'chown -R ubuntu /data/'
}

exec { 'change_group':
	command => 'chgrp -R ubuntu /data/'
}

$str = "server {
    listen 80 default_server;
    listen [::]:80 default_server;
    add_header X-Served-By $HOSTNAME;
    root   /var/www/html;
    index  index.html index.htm;

    location /hbnb_static {
        alias /data/web_static/current;
        index index.html index.htm;
    }

    location /redirect_me {
        return 301 http://cuberule.com/;
    }

    error_page 404 /404.html;
    location /404 {
      root /var/www/html;
      internal;
    }
}"

file { '/etc/nginx/sites-available/default':
	ensure => present,
	content => $str,
}
