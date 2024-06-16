
# Get Paid

## Description
An AI OCR and OpenAI powered workflow that enables analysis of pdfs of employees' salary slips.


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

1)The project first requires conversion of each pdf page to be captured as an image. 

2) The image is then annotated using CVAT tool.

3) After annotations the train subset is fed to a YOLOV8 model for training and the best model is saved.

4) The best model is loaded and inference on the test images is performed. This gives us a Region of Interest(ROI)

5) The ROI is then used by Tesseract, a OCR tool which crops the ROI and then extracts a rough text from it.

6) Then the extracted OCR text is fed to an LLM (OpenAI GPT-3.5-Turbo) which analyzes the text and generates insights.

7) The generated output is then cleaned and processed.

8) The cleaned output can then be exported as a .csv file.
