# 2-execute_a_command.pp

# Explanation: Kill the process named "killmenow" using pkill.

exec { 'killmenow':
  command => 'pkill -f killmenow',
  onlyif  => 'pgrep -f killmenow',
}
