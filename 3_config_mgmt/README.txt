# Using your configuration management tool of choice
# create a policy that manges all aspects of ntp for Ubuntu 14.04.
# Install the package, Generate a configuration file /etc/ntp.conf
# and makes sure the ntpd process is running.
#
# Bonus make sure the policy works on more than just Ubuntu 14.04

This ntp playbook can be ran based on roles on both Redhat and Debian based instances.

#to install ansible on Redhat/Centos
yum install openssl-devel -y
easy_install pip
yum install python-devel -y
yum groupinstall "Development Tools"
pip install paramiko PyYAML Jinja2 httplib2 six
pip install ansible

#to install ansible on Debian
apt-get install software-properties-common
apt-add-repository ppa:ansible/ansible
apt-get update
apt-get install ansible

# to run the playbook
ansible-playbook ntp.yml
from ntp/roles directory
