# Clothes detector
Microservice detecting clothes on given image using:
![](https://dl.fbaipublicfiles.com/detectron2/Detectron2-Logo-Horz.png)

## Download model
Download model from [here](https://drive.google.com/drive/folders/14SHB5GhqrWO1hA-gs1hC2FL_cX3LLRAz?usp=sharing) and place it in *models* dir.
Examplary download using [gdown](https://pypi.org/project/gdown/) tool:  
`mkdir models && gdown -O ./models/model.pth --id google_drive_id`
### Quick note
Model architecture and other details can be found in the following repository https://github.com/pawelbeza/ClothesDetectorModel
## Build  
`docker build -t clothes-detector .`

## Run container

### using CPU
`docker run --rm -p 8080:8080 --name clothes-detector clothes-detector`

### using GPU
`docker run --gpus all --rm -p 8080:8080 --name clothes-detector clothes-detector`
#### Quick note
[nvidia-container-toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html) package is needed to run container with GPU support

## Visualize predictions
```
import cv2
import requests

from PIL import Image
from detectron2.utils.visualizer import Visualizer
from detectron2.data import detection_utils as utils

URL = "IP:8080/detect"
files = {"image": open(filename, 'rb')}

res = requests.post(url=URL, files=files).json()

img = cv2.imread(filename)
img = utils.convert_image_to_rgb(img, 'BGR')

visualizer = Visualizer(img)
out = visualizer.overlay_instances(
    labels=res['classes'],
    boxes=res['boxes']
)

img_pil = Image.fromarray(out.get_image(), 'RGB')
img_pil.show()
```
![](https://user-images.githubusercontent.com/43823276/123514154-b5956180-d691-11eb-9e32-cb15716033ef.jpg)
