#
# DHCP services
#
FROM almalinux:9
MAINTAINER chris@chr.is
# Avoid using mirrors.tummy.com which is slow as f&#$
#RUN for i in /etc/yum.repos.d/*.repo; do sed -i {s/^mirrorlist/#mirrorlist/} $i; done && for i in /etc/yum.repos.d/*.repo; do sed -i {s/^#baseurl=http:\\/\\/mirror\\.centos\\.org/baseurl=https:\\/\\/mirror.rackspace.com/} $i; done
RUN dnf --verbose update -y
RUN dnf --verbose install -y dhcp-server && rm -rf /etc/dhcp/*
WORKDIR /etc/dhcp
CMD /usr/sbin/dhcpd -d -cf /etc/dhcp/dhcpd.conf -user dhcpd -group dhcpd
