FROM alpine:latest

# Установка пакетов с помощью apk
RUN apk update && \
    apk add --no-cache \
    build-base

# Добавление пользователя
RUN adduser -D user && \
    echo "user ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

# Установка рабочего каталога
WORKDIR /app

# Команда по умолчанию
CMD ["/bin/sh"]

# start 'C:\Program Files\Docker\Docker\Docker Desktop.exe'
# docker build -t myimage .
# docker pull alpine:latest
# docker save -o myimage.tar myimage:latest
# https://hub.docker.com/ - репозиторий образов
