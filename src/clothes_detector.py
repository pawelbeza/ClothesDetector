import os
import werkzeug
import cv2
import numpy as np
import torch

from flask_restful import reqparse, Resource

from detectron2 import model_zoo
from detectron2.config import get_cfg
from detectron2.engine import DefaultPredictor


class ClothesDetector(Resource):
    clothes_categories = ['short_sleeved_shirt', 'long_sleeved_shirt', 'short_sleeved_outwear', 'long_sleeved_outwear',
                          'vest', 'sling', 'shorts', 'trousers', 'skirt', 'short_sleeved_dress', 'long_sleeved_dress',
                          'vest_dress', 'sling_dress']

    def __init__(self, model_path=str(os.environ.get('MODEL_PATH', '../models/model.pth'))):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('image', type=werkzeug.datastructures.FileStorage, required=True, location='files')

        cfg = get_cfg()
        cfg.merge_from_file(model_zoo.get_config_file("COCO-Detection/faster_rcnn_R_101_FPN_3x.yaml"))
        cfg.MODEL.WEIGHTS = model_path
        cfg.MODEL.ROI_HEADS.SCORE_THRESH_TEST = 0.5
        cfg.MODEL.ROI_HEADS.NUM_CLASSES = 13
        cfg.MODEL.DEVICE = 'cuda' if torch.cuda.is_available() else 'cpu'

        self.model = DefaultPredictor(cfg)

    def post(self):
        # read image file string data
        image_str = self.parser.parse_args().get('image').read()
        # convert string data to numpy array
        np_img = np.fromstring(image_str, np.uint8)
        # convert numpy array to image
        img = cv2.imdecode(np_img, cv2.IMREAD_UNCHANGED)

        predictions = self.model(img)['instances']
        boxes = predictions.pred_boxes.tensor.tolist() if predictions.has("pred_boxes") else None
        scores = predictions.scores.tolist() if predictions.has("scores") else None
        class_indexes = predictions.pred_classes.tolist() if predictions.has("pred_classes") else None

        class_names = [self.clothes_categories[x] for x in class_indexes]

        return {
            'boxes': boxes,
            'classes': class_names,
            'scores': scores
        }
