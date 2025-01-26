#!/usr/bin/env bash
# SSH config using puppet

file  { '/home/ubuntu/.ssh/config':
  ensure  => 'file',
  content => @("END"),
    Host server-alias
      HostName 100.26.171.159
      User ubuntu
      IdentifyFile ~/.ssh/school
      PasswordAuthentication no
    | END
  mode    => '0644',    
  owner   => 'ubuntu',
  group   => 'ubuntu',
}
