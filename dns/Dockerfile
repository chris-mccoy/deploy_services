#
# DNS services for pxe.chr.is
#
# How to build this container:
# 
# docker build . -t dns
#
# How to run this container:
#
# docker kill dns
# docker rm dns
# docker run -d --restart always --name dns --net host -v /srv/deploy/dns/var/named:/var/named -v /srv/deploy/dns/etc/named.conf:/etc/named.conf dns
#
#
FROM centos:7
MAINTAINER asig@asig.io
RUN yum update -y && yum install -y bind iproute
WORKDIR /var/named
CMD /usr/sbin/named -4 -c /etc/named.conf -g -u named

