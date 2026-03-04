# --- Stage 1: Build Stage ---
FROM gcc:12 AS builder
WORKDIR /app
COPY . .
RUN apt-get update

RUN apt-get update && apt-get install -y \
    build-essential \
    cmake 

RUN cmake --version

RUN mkdir build

RUN apt-get install -y python3-dev

WORKDIR /app/build

RUN cmake ..

RUN make

#RUN apt-get update && apt-get install -y \
#    build-essential \
#    python3-pip 

#RUN apt install python3-numpy
RUN apt-get -y install python3-django

WORKDIR /app/server

EXPOSE 8000

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
#WORKDIR /app
#CMD ["python3", "ex.py"]

#CMD ["ctest"]



