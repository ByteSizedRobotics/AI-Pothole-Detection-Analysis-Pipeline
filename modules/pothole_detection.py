import torch

class PotholeDetection:
    def __init__(self, config):
        self.config = config
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        self._init_model()
        
    def _init_model(self):
        """
        Initialization of Pothole Detection YOLOv5s model with custom trained weights.
        """
        print(f"Initializing Pothole Detector")
        model = torch.hub.load('ultralytics/yolov5', 'custom', path=self.config.POTHOLE_MODEL_PATH).to(self.device)
        self.model = model

        
    def detect(self, image):
        """
        Detect the potholes in the given image. This returns a list of detections, where each detection 
        is in the format: (confidence, [x1, y1, x2, y2])
        """       
        detections = self.model(image)
        
        # print(f"Detected {len(detections.xyxy[0].tolist())} potholes (placeholder)")
        return detections