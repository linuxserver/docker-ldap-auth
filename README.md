[![linuxserver.io](https://raw.githubusercontent.com/linuxserver/docker-templates/master/linuxserver.io/img/linuxserver_medium.png)](https://linuxserver.io)

The [LinuxServer.io](https://linuxserver.io) team brings you another container release featuring :-

 * regular and timely application updates
 * easy user mappings (PGID, PUID)
 * custom base image with s6 overlay
 * weekly base OS updates with common layers across the entire LinuxServer.io ecosystem to minimise space usage, down time and bandwidth
 * regular security updates

Find us at:
* [Discord](https://discord.gg/YWrKVTn) - realtime support / chat with the community and the team.
* [IRC](https://irc.linuxserver.io) - on freenode at `#linuxserver.io`. Our primary support channel is Discord.
* [Blog](https://blog.linuxserver.io) - all the things you can do with our containers including How-To guides, opinions and much more!
* [Podcast](https://podcast.linuxserver.io) - on hiatus. Coming back soon (late 2018).

# PSA: Changes are happening

From August 2018 onwards, Linuxserver are in the midst of switching to a new CI platform which will enable us to build and release multiple architectures under a single repo. To this end, existing images for `arm64` and `armhf` builds are being deprecated. They are replaced by a manifest file in each container which automatically pulls the correct image for your architecture. You'll also be able to pull based on a specific architecture tag.

TLDR: Multi-arch support is changing from multiple repos to one repo per container image.

# [linuxserver/ldap-auth](https://github.com/linuxserver/docker-ldap-auth)
[![](https://images.microbadger.com/badges/version/linuxserver/ldap-auth.svg)](https://microbadger.com/images/linuxserver/ldap-auth "Get your own version badge on microbadger.com")
[![](https://images.microbadger.com/badges/image/linuxserver/ldap-auth.svg)](https://microbadger.com/images/linuxserver/ldap-auth "Get your own version badge on microbadger.com")
![Docker Pulls](https://img.shields.io/docker/pulls/linuxserver/ldap-auth.svg)
![Docker Stars](https://img.shields.io/docker/stars/linuxserver/ldap-auth.svg)

[Ldap-auth](https://github.com/nginxinc/nginx-ldap-auth) software is for authenticating users who request protected resources from servers proxied by nginx. It includes a daemon (ldap-auth) that communicates with an authentication server, and a webserver daemon that generates an authentication cookie based on the user’s credentials. The daemons are written in Python for use with a Lightweight Directory Access Protocol (LDAP) authentication server (OpenLDAP or Microsoft Windows Active Directory 2003 and 2012).

[![ldap-auth](https://jumpcloud.com/wp-content/uploads/2016/12/LDAP_Logo-1420591101.jpg)](https://github.com/nginxinc/nginx-ldap-auth)

## Supported Architectures

Our images support multiple architectures such as `X86-64`, `arm64` and `armhf`. We utilise the docker manifest for multi-platform awareness. More information is available from docker [here](https://github.com/docker/distribution/blob/master/docs/spec/manifest-v2-2.md#manifest-list). 

The architectures supported by this image are:

| Architecture | Tag |
| :----: | --- |
| X86-64 | amd64-latest |
| arm64 | arm64v8-latest |
| armhf | arm32v6-latest |

## Usage

Here are some example snippets to help you get started creating a container.

### docker

```
docker create \
  --name=ldap-auth \
  -e TZ=Europe/London \
  -p 8888:8888 \
  -p 9000:9000 \
  linuxserver/ldap-auth
```


### docker-compose

Compatible with docker-compose v2 schemas.

```
---
version: "2"
services:
  ldap-auth:
    image: linuxserver/ldap-auth
    container_name: ldap-auth
      - TZ=Europe/London
    ports:
      - 8888:8888
      - 9000:9000
    mem_limit: 4096m
    restart: unless-stopped
```

## Parameters

Container images are configured using parameters passed at runtime (such as those above). These parameters are separated by a colon and indicate `<external>:<internal>` respectively. For example, `-p 8080:80` would expose port `80` from inside the container to be accessible from the host's IP on port `8080` outside the container.

| Parameter | Function |
| :----: | --- |
| `-p 8888` | the port for ldap auth daemon |
| `-p 9000` | the port for ldap login page |
| `-e TZ=Europe/London` | Specify a timezone to use EG Europe/London |


&nbsp;
## Application Setup

- This container itself does not have any settings and it relies on the pertinent information passed through in http headers of incoming requests. Make sure that your webserver is set up with the right config.
- Here's a sample config: [nginx-ldap-auth.conf](https://github.com/nginxinc/nginx-ldap-auth/blob/master/nginx-ldap-auth.conf).



## Support Info

* Shell access whilst the container is running: `docker exec -it ldap-auth /bin/bash`
* To monitor the logs of the container in realtime: `docker logs -f ldap-auth`
* container version number 
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' ldap-auth`
* image version number
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' linuxserver/ldap-auth`

## Versions

* **18.09.18:** - Update pip
* **14.09.18:** - Add TZ parameter, remove unnecessary PUID/PGID params
* **11.08.18:** - Initial release.
