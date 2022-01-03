#Sets up your client SSH configuration file
exec { '/etc/ssh/ssh_config':
  path    => ['/usr/bin', '/bin'],
  command => 'echo "IdentityFile ~/.ssh/school" >> /etc/ssh/ssh_config; echo "PasswordAuthentication no" >> /etc/ssh/ssh_config',
}
