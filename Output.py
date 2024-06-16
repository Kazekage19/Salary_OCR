from dotenv import load_dotenv, find_dotenv
import json 
load_dotenv(find_dotenv())
from langchain_community.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import torch
import pandas as pd
import os
import ast

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
template = """
This is an OCR Result from an Employee's Salary Slip. You are an experienced accountant expert at handling financials .Read and understand the result and return a Python dictionary with the following fields: ['Employee Name' ,'Employer Name', 'Basic or Gross Pay' , 'Bonus or Rewards' , 'Tax and other deductions' , 'Net Pay']. If any field is not available or ambiguous assign 'NA' value to it. Calculate the NET PAY if not mentioned.
{text}
RETURN ONLY THE DICTIONARY WITH A VALUE OF NET PAY. NOTHING ELSE. ALSO MAKE SURE ALL VALUES ARE VALID PYTHON LITERAL.
"""
ocr_results_file = 'ocr_results.txt'
OCRs= ''
with open(ocr_results_file, 'r') as f:
    OCRs = f.read()
OCR_data = OCRs.split('##')
OCR_data = [line.strip() for line in OCR_data]

prompt = PromptTemplate(
    input_variables=["text"],
    template=template
)

llm = ChatOpenAI(model_name='gpt-3.5-turbo', temperature=0.0)
chain = LLMChain(llm=llm, prompt=prompt)

data = []
for count,text in enumerate(OCR_data):
    result = chain.invoke(text)
    res=dict(result)
    # print(count)
    # print(res['text'] , end = '\n\n')
    data.append(res['text'])
details_path = 'details.txt'
with open(details_path, 'w') as f:
    f.writelines(data)