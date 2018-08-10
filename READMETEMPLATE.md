[linuxserverurl]: https://linuxserver.io
[forumurl]: https://forum.linuxserver.io
[ircurl]: https://www.linuxserver.io/irc/
[appurl]: www.example.com
[dockerfileurl]: https://github.com/linuxserver/docker-ldap-auth/blob/master/Dockerfile
[hub]: https://hub.docker.com/r/ldap-auth/



[![linuxserver.io](https://raw.githubusercontent.com/linuxserver/docker-templates/master/linuxserver.io/img/linuxserver_medium.png?v=4&s=4000)][linuxserverurl]


## Contact information:- 

| Type | Address/Details | 
| :---: | --- |
| Discord | [Discord](https://discord.gg/YWrKVTn) |
| IRC | freenode at `#linuxserver.io` more information at:- [IRC][ircurl]
| Forum | [Linuserver.io forum][forumurl] |

&nbsp;
&nbsp;

The [LinuxServer.io][linuxserverurl] team brings you another image release featuring :-

 + regular and timely application updates
 + easy user mappings
 + custom base image with s6 overlay
 + weekly base OS updates with common layers across the entire LinuxServer.io ecosystem to minimise space usage, down time and bandwidth
 + security updates

# linuxserver/ldap-auth

[![Dockerfile-link](https://raw.githubusercontent.com/linuxserver/docker-templates/master/linuxserver.io/img/Dockerfile-Link-green.png)][dockerfileurl]

The ldap-auth software is for authenticating users who request protected resources from servers proxied by nginx. It includes a daemon (ldap-auth) that communicates with an authentication server, and a webserver daemon that generates an authentication cookie based on the user’s credentials. The daemons are written in Python for use with a Lightweight Directory Access Protocol (LDAP) authentication server (OpenLDAP or Microsoft Windows Active Directory 2003 and 2012).


&nbsp;

## Usage

```
docker create \
  --name=ldap-auth \
  -p 8888:8888 \
  -p 9000:9000 \
  linuxserver/ldap-auth
```

&nbsp;

## Parameters

The parameters are split into two halves, separated by a colon, the left hand side representing the host and the right the container side. 
For example with a port -p external:internal - what this shows is the port mapping from internal to external of the container.
So -p 8080:80 would expose port 80 from inside the container to be accessible from the host's IP on port 8080
http://192.168.x.x:8080 would show you what's running INSIDE the container on port 80.

NOTE: This container does not save any data that should be persistent and therefore there is no mapping for a `/config` folder.


| Parameter | Function |
| :---: | --- |
| `-p 8888` | the port for ldap auth daemon |
| `-p 9000` | the port for ldap login page |


&nbsp;

## Setting up the application

This container itself does not have any settings and it relies on the pertinent information passed in the form of http headers in incoming requests. Make sure that your webserver is set up with the right config. Here's a sample config: https://github.com/nginxinc/nginx-ldap-auth/blob/master/nginx-ldap-auth.conf


&nbsp;

## Container access and information.

| Function | Command |
| :--- | :--- |
| Shell access (live container) | `docker exec -it ldap-auth /bin/bash` |
| Realtime container logs | `docker logs -f ldap-auth` |
| Container version | `docker inspect -f '{{ index .Config.Labels "build_version" }}' ldap-auth` |
| Image version |  `docker inspect -f '{{ index .Config.Labels "build_version" }}' linuxserver/ldap-auth` |
| Dockerfile | [Dockerfile][dockerfileurl] |

&nbsp;

## Changelog

|  Date | Changes |
| :---: | --- |
| dd.MM.yy |  Initial Release. |
