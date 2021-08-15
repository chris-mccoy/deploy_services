#
# WWW services
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
