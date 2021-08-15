#
# Managed by Ansible: last modified on 2018-09-07 15:49:43 EDT
#
#
# DHCP services
#
#
# How to run this container:
#
# docker run -d --restart always --name dhcp --net host -v /srv/deploy/dhcp:/etc/dhcp dhcp
#
# How to build this container:
#
# docker build . -t dhcp
#
FROM centos:7
MAINTAINER asig@asig.io
RUN yum update -y
RUN yum install -y dhcp iproute && rm -rf /etc/dhcp/*
WORKDIR /etc/dhcp
CMD /usr/sbin/dhcpd -d -cf /etc/dhcp/dhcpd.conf -user dhcpd -group dhcpd
