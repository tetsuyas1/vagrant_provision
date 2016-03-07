#!/usr/bin/env bash

if ! [ `which ansible` ]; then
    yum install -y  http://dl.fedoraproject.org/pub/epel/6/x86_64/epel-release-6-8.noarch.rpm
    yum install -y install ansible
fi

sudo cp work/hosts /tmp/temp_hosts
sudo chmod -x /tmp/temp_hosts
bash -c "ansible-playbook work/playbook.yml --inventory-file=/tmp/temp_hosts"
