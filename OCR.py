import pytesseract
from ultralytics import YOLO
import cv2
import torch
import glob
import pandas as pd

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model_path = 'C:\\Users\\aksha\\Desktop\\DS Projects\\Lumberfi\\best.pt'
model = YOLO(model_path).to(device)
pytesseract.pytesseract.tesseract_cmd = r'./PyTesseract/tesseract.exe'
test_images = glob.glob('./yolo_dataset/images/train/*.png')
OCRs = []
ocr_results_file = 'ocr_results.txt'
def perform_ocr(cropped_image):
    try:
        text = pytesseract.image_to_string(cropped_image)
        return text
    except Exception as e:
        print(f"OCR failed: {e}")
        return ""

def process_image(image_path):
    detections = model(image_path)
    img = cv2.imread(image_path)
    for result in detections:
        boxes = result.boxes.xyxy.cpu().numpy()
        for box in boxes:
            x1, y1, x2, y2 = map(int, box[:4])
            cropped_img = img[y1:y2, x1:x2]
            text = perform_ocr(cropped_img)
            OCRs.append(text.strip() + '##' + '\n')    
for img_path in test_images:
    process_image(img_path)
    
with open(ocr_results_file, 'w') as f:
    f.writelines(OCRs)


