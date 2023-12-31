# light weight for linux OS -> alpine
FROM python:3.11-alpine

WORKDIR /usr/src/app

# prevent python from writing .pyc file
ENV PYTHONDONTWRITEBYTECODE 1
# ensure python output is sent directly to the terminal without bufffering
ENV PYHTONUNBUFFERED 1

# Install postgres client
RUN apk add --update --no-cache postgresql-client
# Install individual dependencies so that we could avoid installing extra packages to the container
RUN apk add --update --no-cache --virtual .tmp-build-deps \
	gcc libc-dev linux-headers postgresql-dev
# Remove dependencies
RUN apk del .tmp-build-deps

# install pip
RUN pip install --upgrade pip
# copy requirements files
COPY ./requirements.txt /usr/src/app/
# install packages from the requirements
RUN pip install -r requirements.txt
# copy linux shell scripts
COPY ./entrypoint.sh /usr/src/app/entrypoint.sh

# copy project files
COPY . /usr/src/app/

# run when container starts
ENTRYPOINT [ "/usr/src/app/entrypoint.sh" ]