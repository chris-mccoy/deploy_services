#
# How to build this container:
# 
# docker build . --build-arg vault_release=1.5.3 -t vault:1.5.3
#
# How to run this container:
#
# docker kill vault
# docker rm vault
# docker run -d --net=host --restart=always --cap-add IPC_LOCK --name vault -v /srv/deploy/vault:/vault vault:1.5.3
#
#

FROM alpine:3.12
MAINTAINER Jeff Mitchell <jeff@hashicorp.com> (@jefferai)

# This is the release of Vault to pull in.
ARG vault_release=1.5.3
ENV VAULT_VERSION=$vault_release

# Create a vault user and group first so the IDs get set the same way,
# even as the rest of this may change over time.
RUN addgroup -g 998 vault && \
    adduser -u 998 -S -G vault vault

# Set up certificates, our base tools, and Vault.
RUN apk add --no-cache ca-certificates gnupg openssl libcap su-exec dumb-init wget && \
    gpg --keyserver pool.sks-keyservers.net --recv-keys 91A6E7F85D05C65630BEF18951852D87348FFC4C && \
    mkdir -p /tmp/build && \
    cd /tmp/build && \
    wget https://releases.hashicorp.com/vault/${VAULT_VERSION}/vault_${VAULT_VERSION}_linux_amd64.zip && \
    wget https://releases.hashicorp.com/vault/${VAULT_VERSION}/vault_${VAULT_VERSION}_SHA256SUMS && \
    wget https://releases.hashicorp.com/vault/${VAULT_VERSION}/vault_${VAULT_VERSION}_SHA256SUMS.sig && \
    gpg --batch --verify vault_${VAULT_VERSION}_SHA256SUMS.sig vault_${VAULT_VERSION}_SHA256SUMS && \
    grep vault_${VAULT_VERSION}_linux_amd64.zip vault_${VAULT_VERSION}_SHA256SUMS | sha256sum -c && \
    unzip -d /bin vault_${VAULT_VERSION}_linux_amd64.zip && \
    cd /tmp && \
    rm -rf /tmp/build && \
    apk del gnupg openssl
#    find /root && \
#    rm -rf /root/.gnupg

# /vault/logs is made available to use as a location to store audit logs, if
# desired; /vault/file is made available to use as a location with the file
# storage backend, if desired; the server will be started with /vault/config as
# the configuration directory so you can add additional config files in that
# location.
#RUN mkdir -p /vault/logs && \
#    mkdir -p /vault/file && \
#    mkdir -p /vault/config && \
#    chown -R vault:vault /vault

# Expose the logs directory as a volume since there's potentially long-running
# state in there
#VOLUME /vault/logs

# Expose the file directory as a volume since there's potentially long-running
# state in there
#VOLUME /vault/file

# 8200/tcp is the primary interface that applications use to interact with
# Vault.
EXPOSE 8200

# The entry point script uses dumb-init as the top-level process to reap any
# zombie processes created by Vault sub-processes.
#
# For production derivatives of this container, you shoud add the IPC_LOCK
# capability so that Vault can mlock memory.
COPY docker-entrypoint.sh /usr/local/bin/docker-entrypoint.sh
RUN chmod a+x /usr/local/bin/docker-entrypoint.sh
ENTRYPOINT ["/usr/local/bin/docker-entrypoint.sh"]

# By default you'll get a single-node development server that stores everything
# in RAM and bootstraps itself. Don't use this configuration for production.
#CMD ["server", "-dev"]
CMD ["server"]
