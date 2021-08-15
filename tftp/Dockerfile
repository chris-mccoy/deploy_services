#
# Managed by Ansible: last modified on 2018-09-07 22:30:21 EDT
#
#
# TFTP services
#
# How to build this container:
#
# docker build . -t tftp
#
# How to run this container:
#
# docker run -d --restart always --name tftp --net host -v /srv/deploy/tftp:/srv/tftp tftp
#
FROM ubuntu:16.04
MAINTAINER asig@asig.io
RUN apt update -y && apt upgrade -y && apt install atftpd -y
WORKDIR /srv/tftp
CMD /usr/sbin/atftpd --daemon --no-fork --port 69 --retry-timeout 5 --mcast-port 1758 --mcast-addr 239.239.239.0-255 --mcast-ttl 1 --maxthread 100 --verbose=7 --trace --logfile=/dev/stdout /srv/tftp
