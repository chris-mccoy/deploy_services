#
# bootstrap-vz
#
# Creates a Kali image to boot in OpenStack
#
# *** This container runs privileged so loopback devices work ***
#
# * How to build:
#
# docker build -t bootstrap-vz .
# 
# * How to run:
#
# docker run -it --name bootstrap-vz --privileged -v /dev:/dev -v /share:/share bootstrap-vz bash
# cd ~/bootstrap-vz
# . venv/bin/activate
# bootstrap-vz --debug --pause-on-error ./manifests/sudo-kali.yml
#
# Image is in bootstrap-vz-target
#

FROM ubuntu:16.04
COPY bootstrap-vz /root/bootstrap-vz
RUN apt update && \
    apt install -y debootstrap parted kpartx python-virtualenv vim && \
    ln -s /usr/share/debootstrap/scripts/sid /usr/share/debootstrap/scripts/kali-rolling  && \
    cd /root/bootstrap-vz && \
    virtualenv venv && \
    . venv/bin/activate && \
    pip install .

