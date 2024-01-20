# 0-create_a_file.pp

# Explanation: Create a file in /tmp named 'school' with the given permissions, owner, group, and content.

file { '/tmp/school':
  ensure   => file,
  mode     => '0744',
  owner    => 'www-data',
  group    => 'www-data',
  content  => 'I love Puppet',
}
