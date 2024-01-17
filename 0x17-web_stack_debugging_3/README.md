# 0x17. Web Stack Debugging #3

## Description
Web stack debugging project focusing on troubleshooting and resolving issues in a Wordpress website running on a LAMP stack. The tasks involve using tools like strace to identify the root cause of a 500 Internal Server Error in Apache, fixing the issue, and automating the solution using Puppet.

## Concepts
- Web Server
- Web Stack Debugging

## Requirements
- All files interpreted on Ubuntu 14.04 LTS
- Puppet manifests must pass puppet-lint version 2.1.1 without errors
- Puppet manifests must run without errors
- Puppet manifests must have a comment explaining their purpose
- Puppet manifest files must end with the extension .pp
- Files will be checked with Puppet v3.4

## Installation
To install puppet-lint:

```bash
$ apt-get install -y ruby
$ gem install puppet-lint -v 2.1.1

