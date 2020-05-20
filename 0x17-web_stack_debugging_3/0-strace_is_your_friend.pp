# Search bad extension and repair
exec { 'repair wp-settings':
  command => "sed -i 's/\\/.phpp/\\/.php/g'/var/www/html/wp-settings.php",
  path    => '/bin/',
}
