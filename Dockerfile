FROM centos
LABEL  "name"="ruchi"
RUN dnf install httpd -y
EXPOSE 80
ENTRYPOINT httpd -DFOREGROUND
