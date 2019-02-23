FROM lsiobase/alpine:3.9

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
	libffi-dev \
	openldap-dev \
	python2-dev && \
 echo "**** install runtime packages ****" && \
 apk add --no-cache \
	libffi \
	libldap \
	py2-pip \
	python2 && \
 if [ -z ${LDAP_VERSION+x} ]; then \
  LDAP_INSTALL="python-ldap"; \
 else \
  LDAP_INSTALL="python-ldap==${LDAP_VERSION}"; \
 fi && \
 pip install -U --no-cache-dir \
        pip && \
 pip install -U \
        cryptography \
        ${LDAP_INSTALL} && \
 echo "**** cleanup ****" && \
 apk del --purge \
        build-dependencies && \
 rm -rf \
        /tmp/* \
        /root/.cache/pip

# copy local files
COPY root/ /

# ports and volumes
EXPOSE 8888 9000
