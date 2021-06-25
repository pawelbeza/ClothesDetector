# Clothes detector
Microservice detecting clothes on given image using:
![](https://dl.fbaipublicfiles.com/detectron2/Detectron2-Logo-Horz.png)

## Download model from [here](https://drive.google.com/drive/folders/14SHB5GhqrWO1hA-gs1hC2FL_cX3LLRAz?usp=sharing) and place it in `models` dir
Examplary download using [gdown](https://pypi.org/project/gdown/) tool:  
`mkdir models && gdown -O ./models/model.pth --id google_drive_id`

## Build  
`docker build -t clothes-detector .`

## Run container

### using CPU
`docker run -p 8080:8080 --name clothes-detector clothes-detector`

### using GPU
`docker run --gpus all -p 8080:8080 --name clothes-detector clothes-detector`
#### Quick note
[nvidia-container-toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html) package is needed to run container with GPU support
