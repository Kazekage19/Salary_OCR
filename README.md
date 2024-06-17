
# Get Paid

## Description
An AI OCR and OpenAI powered workflow that enables analysis of pdfs of employees' salary slips.

## Dataset Description
- The dataset consists of ```Salary Slips``` folder , which is a image dataset of Salary slips. These images are converted into pdfs which contain text salary slips(of fake data) and both text and image are combined, some pdfs are just text and some pdfs are just images but most of them contain both in the ```pdfs``` dataset folder.
- Now the each pdf page is captured as an image and stored as ```pdf_images``` . Each image is then uploaded to an annotation tool for annotating the salary slips and the resultant images and labels are labelled as ```yolo dataset``` which you can find in the drive link here :  https://drive.google.com/drive/folders/1cgN6m8kMdD3Yrz6MoElDU9VBC2EVL_oa?usp=drive_link
- In the ```yolo_dataset``` the images and their labels are split into train and test datasets in 1:3 ratio. Then these images are fed to a YoloV8 model.

## Installation

### Get Started
First, clone the repository to your local machine using `git`.

```sh
git clone https://github.com/Kazekage19/Salary_OCR.git
cd Salary_OCR
```
```sh
python -m venv env
```
```sh
pip install -r requirements.txt
```

## Workflow

1) The project first requires conversion of each pdf page to be captured as an image. 

2) The image is then annotated using CVAT tool.

3) After annotations the train subset is fed to a YOLOV8 model for training and the best model is saved.

4) The best model is loaded and inference on the test images is performed. This gives us a Region of Interest(ROI)

5) The ROI is then used by Tesseract, a OCR tool which crops the ROI and then extracts a rough text from it.

6) Then the extracted OCR text is fed to an LLM (OpenAI GPT-3.5-Turbo) which analyzes the text and generates insights.

7) The generated output is then cleaned and processed.

8) The cleaned output can then be exported as a .csv file.
