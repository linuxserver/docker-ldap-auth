FROM ghcr.io/linuxserver/baseimage-alpine:3.15

# set version label
ARG BUILD_DATE
ARG VERSION
ARG LDAP_VERSION
LABEL build_version="Linuxserver.io version:- ${VERSION} Build-date:- ${BUILD_DATE}"
LABEL maintainer="aptalca"

RUN \
  echo "**** install build packages ****" && \
  apk add --no-cache --virtual=build-dependencies \
    build-base \
    cargo \
    libffi-dev \
    openldap-dev \
    python3-dev && \
  echo "**** install runtime packages ****" && \
  apk add --no-cache \
    libffi \
    libldap \
    py3-pip \
    python3 && \
  if [ -z ${LDAP_VERSION+x} ]; then \
    LDAP_INSTALL="python-ldap"; \
  else \
    LDAP_INSTALL="python-ldap==${LDAP_VERSION}"; \
  fi && \
  pip3 install -U --no-cache-dir pip setuptools wheel && \
  pip install -U --no-cache-dir --find-links https://wheel-index.linuxserver.io/alpine-3.15/ \
    cryptography \
    ${LDAP_INSTALL} && \
  echo "**** cleanup ****" && \
  apk del --purge \
    build-dependencies && \
  rm -rf \
    /tmp/* \
    /root/.cache \
    /root/.cargo

# copy local files
COPY root/ /

# ports and volumes
EXPOSE 8888 9000
