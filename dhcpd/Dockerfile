#
# DHCP services
#
FROM centos:8
MAINTAINER chris@chr.is
RUN dnf --verbose update -y
RUN dnf --verbose install -y dhcp-server && rm -rf /etc/dhcp/*
WORKDIR /etc/dhcp
CMD /usr/sbin/dhcpd -d -cf /etc/dhcp/dhcpd.conf -user dhcpd -group dhcpd
