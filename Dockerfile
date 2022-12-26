# syntax=docker/dockerfile:1

FROM ghcr.io/linuxserver/baseimage-alpine:3.17

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
    python3 && \
  if [ -z ${LDAP_VERSION+x} ]; then \
    LDAP_VERSION=$(curl -sL  https://pypi.python.org/pypi/python-ldap/json |jq -r '. | .info.version'); \
  fi && \
  python3 -m ensurepip && \
  pip3 install -U --no-cache-dir \
    pip \
    wheel && \
  pip3 install -U --no-cache-dir --find-links https://wheel-index.linuxserver.io/alpine-3.17/ \
    cryptography \
    python-ldap=="${LDAP_VERSION}" && \
  echo "**** cleanup ****" && \
  apk del --purge \
    build-dependencies && \
  rm -rf \
    /tmp/* \
    $HOME/.cache \
    $HOME/.cargo

# copy local files
COPY root/ /

# ports and volumes
EXPOSE 8888 9000
