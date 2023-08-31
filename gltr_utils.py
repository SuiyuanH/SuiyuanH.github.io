import numpy as np
import json
from glob import glob

def getColorClass(rank):
    if rank < 10:
        return "rank-color-1"
    elif rank < 100:
        return "rank-color-2"
    elif rank < 1000:
        return "rank-color-3"
    else:
        return "rank-color-4"

jsons = glob('gltr_data/*.json') 

def postprocess(token):

    with_space = True
    with_break = token == '[SEP]'
    if token.startswith('##'):
        with_space = False
        token = token[2:]

    if with_space:
        token = '\u0120' + token
    if with_break:
        token = '\u010A' + token
    return token

def process_token (token):
    if token.startswith ('\u010A'):
        token = '\n'+token.lstrip ('\u010A')
    if token.startswith ('\u0120'):
        token = '\n'+token.lstrip ('\u0120')
    return token

def parse_json (path):
    with open (path, 'r', encoding='utf-8') as f:
        content = json.load (f)['result']
    tokens = content ['bpe_strings'][1:]
    topk = content ['real_topk']
    assert len (tokens) == len (topk)
    output = [{'token':process_token (token), 'rank':getColorClass(int (rank))}for token, (rank, _) in zip (tokens, topk)]
    return output
    
def gen_input():
    json_path = np.random.choice (jsons)
    output = parse_json (json_path)
    return output