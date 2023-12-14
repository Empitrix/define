import os, json
from src.models import word_response_parser, WordResponseAPI


PATH = os.path.join(os.getcwd(), "output.json") 
data:dict = {}

with open(PATH, "r") as j_file:
	data = json.load(j_file)[0]


output:WordResponseAPI = word_response_parser(data) 

