# Ensure the PHP module is installed and enabled, then restart Apache

package { 'libapache2-mod-php':
  ensure => installed,
}

exec { 'enable_php_module':
  command => '/usr/sbin/a2enmod php5',
  path    => ['/bin', '/usr/bin', '/sbin', '/usr/sbin'],
  unless  => '/usr/sbin/apache2ctl -M | grep php5',
  notify  => Service['apache2'],
}

service { 'apache2':
  ensure => running,
  enable => true,
  require => Package['libapache2-mod-php'],
}
