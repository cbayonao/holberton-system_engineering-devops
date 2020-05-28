# Reapir NGNIX
exec { 'repair NGINX':
  command => "sed -i 's/15/4096/g' /etc/default/nginx",
  path    => '/bin/',
}

service { 'nginx':
  ensure    => running,
  subscribe => Exec['/etc/default/nginx'],
}
