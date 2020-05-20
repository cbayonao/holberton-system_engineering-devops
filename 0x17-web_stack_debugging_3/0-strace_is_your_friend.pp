# Search bad extension and repair

exec { 'repair wp-settings':
  command => "sed -i 's/\\/class-wp-locale.phpp/\\/class-wp-local
              /var/www/html/wp-settings.php",
}
