import requests
import re

API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-v0.1"
headers = {"Authorization": "Bearer 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"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()


def section1(name, age, retirement_age, life_expectancy):
    output = query({
        "inputs": f"[INST] You are a helpful text generating assistant. Your task is to generate a short paragraph using only the information given, and your analysis of the ages: name: {name}, current age: {age}, retirement age: {retirement_age}, life expectancy: {life_expectancy}, Just analyze the above and generate text based on the analysis: [/INST]",
    })
    print(output)
    out_regex = re.search(r'\[OUT\](.*?)\[/OUT\]|(?:\[OUT\](.*))$', output[0]['generated_text'], re.DOTALL)
    output = out_regex.group(1) or out_regex.group(2)
    return output

def section2(name,savings,income):
    output2 = query({
        "inputs": f"[INST] You are a helpful text generating assistant. Your task is to generate a short paragraph using only the information given: name: {name}, saved amount: Rs. {savings}, income: Rs. {income} per year, Just analyze the above and generate based on the analysis: [/INST]",
    })

    print(output2)
    out_regex = re.search(r'\[OUT\](.*?)\[/OUT\]|(?:\[OUT\](.*))$', output2[0]['generated_text'], re.DOTALL)
    output2 = out_regex.group(1) or out_regex.group(2)
    return output2

def section3a(liv_exp):
    output3 = query({
        "inputs": f"[INST] You are a helpful text generating assistant. Your task is to generate a paragraph on household expenses and the household expense of the client which is Rs. {liv_exp} yearly [/INST]",
    })

    out_regex = re.search(r'\[SOL\]\n\n(.*?)\n\n', output3[0]['generated_text'], re.DOTALL)
    output3 = out_regex.group(1) 
    return output3
    
def section3b(health_exp):    
    output4 = query({
        "inputs": f"[INST] You are a helpful text generating assistant. Your task is to generate a paragraph on healthcare expenses and the healthcare expense of the client which is Rs. {health_exp} yearly [/INST]",
    })
    out_regex = re.search(r'\[SOL\]\n\n(.*?)\n\n', output4[0]['generated_text'], re.DOTALL)
    output4 = out_regex.group(1)
    return output4

def section3c(name,income,misc_exp):
    output5 = query({
		"inputs": f"[INST] You are a helpful text generating assistant. Your task is to generate a very short paragraph strictly on the following information : name: {name}, income: Rs. {income} yearly, miscellaneous expenses: {misc_exp} yearly, Just analyze the above and generate based on the analysis: [/INST]",
	})

    out_regex = re.search(r'\[OUT\](.*?)\[/OUT\]|(?:\[OUT\](.*))$', output5[0]['generated_text'], re.DOTALL)
    output5 = out_regex.group(1) or out_regex.group(2)
    return output5

def section3d():
    output6 = query({
		"inputs": "[INST] You are a helpful text generating assistant. Your task is to generate maximum a very short paragraph on longetivity retirement scenario [/INST]",
	})

    out_regex = re.search(r'\[OUTPUT\]\n\n(.*?)\n\n', output6[0]['generated_text'], re.DOTALL)
    output6 = out_regex.group(1)
    return output6

# section1("Janice Abraham",54,60,80)
	
