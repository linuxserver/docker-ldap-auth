FROM lsiobase/alpine.python:3.7

# set version label
ARG BUILD_DATE
ARG VERSION
LABEL build_version="Linuxserver.io version:- ${VERSION} Build-date:- ${BUILD_DATE}"
LABEL maintainer="aptalca"

# install packages
RUN \
 apk add --no-cache \
	libldap && \
 apk add --no-cache --virtual=build-dependencies \
	build-base \
	openldap-dev \
	python2-dev \
	python3-dev && \
 pip install --no-cache-dir \
	cryptography \
	python-ldap && \
 echo "**** remove build dependencies ****" && \
 apk del --purge \
	build-dependencies && \
 rm -rf \
	/tmp/*

# copy local files
COPY root/ /

# ports and volumes
EXPOSE 8888 9000
