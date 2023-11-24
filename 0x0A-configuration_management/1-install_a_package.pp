# This installs flask
package { 'flask':
  ensure   => 'present',
  provider => 'pip3',
}
