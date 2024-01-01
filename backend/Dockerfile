# light weight for linux OS -> alpine
FROM python:3.11

WORKDIR /code

# prevent python from writing .pyc file
ENV PYTHONDONTWRITEBYTECODE 1
# ensure python output is sent directly to the terminal without bufffering
ENV PYHTONUNBUFFERED 1


# install pip
RUN pip install --upgrade pip
# copy requirements files
COPY ./requirements.txt /code/
# install packages from the requirements
RUN pip install -r requirements.txt
# copy linux shell scripts
COPY ./startup.sh /code/startup.sh

# copy project files
COPY . /code/

# run when container starts
ENTRYPOINT [ "./startup.sh" ]