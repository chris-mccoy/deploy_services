#
# DNS services
#
FROM centos:8
MAINTAINER chris@chr.is
# Avoid using mirrors.tummy.com which is slow as f&#$
RUN for i in /etc/yum.repos.d/*.repo; do sed -i {s/^mirrorlist/#mirrorlist/} $i; done && for i in /etc/yum.repos.d/*.repo; do sed -i {s/^#baseurl=http:\\/\\/mirror\\.centos\\.org/baseurl=https:\\/\\/packages.oit.ncsu.edu/} $i; done
RUN dnf --verbose update -y
RUN dnf --verbose install -y bind bind-utils
WORKDIR /var/named
EXPOSE 53/udp 53/tcp
CMD /usr/sbin/named -4 -c /etc/named.conf -g -u named

