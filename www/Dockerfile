#
# Managed by Ansible: last modified on 2018-09-07 20:47:25 EDT
#
#
# WWW services
#
# How to build this container:
#
# docker build . -t www
#
# How to run this container:
#
# docker run -d --restart always --name www --net host -v /srv/deploy/www:/var/www/html -v /srv/img:/srv/img www
#
#
FROM ubuntu:20.04
MAINTAINER chris@chr.is
RUN apt update -y && apt upgrade -y
RUN apt install nginx -y
RUN rm -rf /var/www/html
WORKDIR /var/www/html
COPY site-default /etc/nginx/sites-available/default
EXPOSE 80/tcp
EXPOSE 443/tcp
CMD /usr/sbin/nginx -g 'daemon off; master_process on; error_log /dev/stdout info;'
