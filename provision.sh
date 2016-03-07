#!/usr/bin/env bash

if ! [ `which ansible` ]; then
    yum install -y  http://dl.fedoraproject.org/pub/epel/6/x86_64/epel-release-6-8.noarch.rpm
    yum install -y install ansible
fi

ansible-playbook work/playbook.yml -i work/hosts
