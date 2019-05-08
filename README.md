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

# [linuxserver/ldap-auth](https://github.com/linuxserver/docker-ldap-auth)
[![](https://img.shields.io/discord/354974912613449730.svg?logo=discord&label=LSIO%20Discord&style=flat-square)](https://discord.gg/YWrKVTn)
[![](https://images.microbadger.com/badges/version/linuxserver/ldap-auth.svg)](https://microbadger.com/images/linuxserver/ldap-auth "Get your own version badge on microbadger.com")
[![](https://images.microbadger.com/badges/image/linuxserver/ldap-auth.svg)](https://microbadger.com/images/linuxserver/ldap-auth "Get your own version badge on microbadger.com")
![Docker Pulls](https://img.shields.io/docker/pulls/linuxserver/ldap-auth.svg)
![Docker Stars](https://img.shields.io/docker/stars/linuxserver/ldap-auth.svg)
[![Build Status](https://ci.linuxserver.io/buildStatus/icon?job=Docker-Pipeline-Builders/docker-ldap-auth/master)](https://ci.linuxserver.io/job/Docker-Pipeline-Builders/job/docker-ldap-auth/job/master/)
[![](https://lsio-ci.ams3.digitaloceanspaces.com/linuxserver/ldap-auth/latest/badge.svg)](https://lsio-ci.ams3.digitaloceanspaces.com/linuxserver/ldap-auth/latest/index.html)

[Ldap-auth](https://github.com/nginxinc/nginx-ldap-auth) software is for authenticating users who request protected resources from servers proxied by nginx. It includes a daemon (ldap-auth) that communicates with an authentication server, and a webserver daemon that generates an authentication cookie based on the user’s credentials. The daemons are written in Python for use with a Lightweight Directory Access Protocol (LDAP) authentication server (OpenLDAP or Microsoft Windows Active Directory 2003 and 2012).

[![ldap-auth](https://jumpcloud.com/wp-content/uploads/2016/12/LDAP_Logo-1420591101.jpg)](https://github.com/nginxinc/nginx-ldap-auth)

## Supported Architectures

Our images support multiple architectures such as `x86-64`, `arm64` and `armhf`. We utilise the docker manifest for multi-platform awareness. More information is available from docker [here](https://github.com/docker/distribution/blob/master/docs/spec/manifest-v2-2.md#manifest-list) and our announcement [here](https://blog.linuxserver.io/2019/02/21/the-lsio-pipeline-project/). 

Simply pulling `linuxserver/ldap-auth` should retrieve the correct image for your arch, but you can also pull specific arch images via tags.

The architectures supported by this image are:

| Architecture | Tag |
| :----: | --- |
| x86-64 | amd64-latest |
| arm64 | arm64v8-latest |
| armhf | arm32v7-latest |


## Usage

Here are some example snippets to help you get started creating a container.

### docker

```
docker create \
  --name=ldap-auth \
  -e TZ=Europe/London \
  -p 8888:8888 \
  -p 9000:9000 \
  --restart unless-stopped \
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
    environment:
      - TZ=Europe/London
    ports:
      - 8888:8888
      - 9000:9000
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

## Updating Info

Most of our images are static, versioned, and require an image update and container recreation to update the app inside. With some exceptions (ie. nextcloud, plex), we do not recommend or support updating apps inside the container. Please consult the [Application Setup](#application-setup) section above to see if it is recommended for the image.  
  
Below are the instructions for updating containers:  
  
### Via Docker Run/Create
* Update the image: `docker pull linuxserver/ldap-auth`
* Stop the running container: `docker stop ldap-auth`
* Delete the container: `docker rm ldap-auth`
* Recreate a new container with the same docker create parameters as instructed above (if mapped correctly to a host folder, your `/config` folder and settings will be preserved)
* Start the new container: `docker start ldap-auth`
* You can also remove the old dangling images: `docker image prune`

### Via Docker Compose
* Update all images: `docker-compose pull`
  * or update a single image: `docker-compose pull ldap-auth`
* Let compose update all containers as necessary: `docker-compose up -d`
  * or update a single container: `docker-compose up -d ldap-auth`
* You can also remove the old dangling images: `docker image prune`

### Via Watchtower auto-updater (especially useful if you don't remember the original parameters)
* Pull the latest image at its tag and replace it with the same env variables in one run:
  ```
  docker run --rm \
  -v /var/run/docker.sock:/var/run/docker.sock \
  containrrr/watchtower \
  --run-once ldap-auth
  ```
* You can also remove the old dangling images: `docker image prune`

## Building locally

If you want to make local modifications to these images for development purposes or just to customize the logic: 
```
git clone https://github.com/linuxserver/docker-ldap-auth.git
cd docker-ldap-auth
docker build \
  --no-cache \
  --pull \
  -t linuxserver/ldap-auth:latest .
```

The ARM variants can be built on x86_64 hardware using `multiarch/qemu-user-static`
```
docker run --rm --privileged multiarch/qemu-user-static:register --reset
```

Once registered you can define the dockerfile to use with `-f Dockerfile.aarch64`.

## Versions

* **23.03.19:** - Switching to new Base images, shift to arm32v7 tag.
* **22.02.19:** - Rebasing to alpine 3.9.
* **18.09.18:** - Update pip
* **14.09.18:** - Add TZ parameter, remove unnecessary PUID/PGID params
* **11.08.18:** - Initial release.
