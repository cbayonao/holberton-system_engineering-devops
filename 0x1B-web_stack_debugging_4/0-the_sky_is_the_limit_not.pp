# Increase max open files
exec { 'repair NGINX':
  command => "sed -i 's/15/4096/g' /etc/default/nginx",
  path    => '/bin/',
}

service { 'repair NGINX':
  ensure    => running,
  subscribe => Exec['/etc/default/nginx'],
}
