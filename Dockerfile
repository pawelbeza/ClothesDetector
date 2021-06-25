FROM nvidia/cuda:10.1-devel

COPY models/ models/
COPY requirements requirements/requirements
COPY src/ app/

RUN apt-get update
RUN apt-get install python3-dev python3-pip ffmpeg libsm6 libxext6  -y

RUN pip3 install --upgrade setuptools
RUN pip3 install --upgrade pip
RUN pip3 install -r /requirements/requirements
RUN python3 -m pip install detectron2==0.4 -f \
    https://dl.fbaipublicfiles.com/detectron2/wheels/cu101/torch1.8/index.html

WORKDIR /app

ENV PORT 8080
ENV MODEL_PATH '/models/model.pth'

CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 app:app