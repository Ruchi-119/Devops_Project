FROM ubuntu
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get -y install  apache2
RUN apt-get install apache2-utils -y
RUN apt-get clean
LABEL "author.name" = "Ruchi jain"
LABEL "author.email" = "jnru501@hmail.com"

EXPOSE 80
WORKDIR /var/www/html/
ADD index.html  .
ENTRYPOINT apache2ctl -D FOREGROUND
