FROM python:3.9

# SET WORK DIRECTORY
WORKDIR /usr/src/app

# COPY THE DEPENDENCIES TO THE WORKDIR
COPY ./requirements.txt ./

# INSTALL DEPENDENCIES
RUN pip install --no-cache-dir -r requirements.txt

# COPY APPLICATION TO THE WORKDIR
COPY . . 
