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
FROM ubuntu:22.04
MAINTAINER chris@chr.is
RUN apt update -y && apt upgrade -y
#RUN apt install atftpd -y
RUN apt install tftpd-hpa -y
WORKDIR /srv/tftp
#CMD /usr/sbin/atftpd --daemon --no-fork --port 69 --retry-timeout 5 --mcast-port 1758 --mcast-addr 239.239.239.0-255 --mcast-ttl 1 --maxthread 100 --verbose=7 --trace --logfile=/dev/stdout /srv/tftp
CMD /usr/sbin/in.tftpd --foreground --create --secure --verbosity 7 --port-range 6969:6979 /srv/tftp

