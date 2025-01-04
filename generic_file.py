# Author: Dhaval Patel. Codebasics YouTube Channel

import re

def get_str_from_food_dict(food_dict: dict):
    result = ", ".join([f"{int(value)} {key}" for key, value in food_dict.items()])
    return result


def extract_session_id(session_str: str):
    match = re.search(r"/sessions/(.*?)/contexts/", session_str)
    if match:
        extracted_string = match.group(0)
        return extracted_string

    return ""
'''
import re
def extract_session_id(session_str:str):
    match=re.search(r"/sessions/(.*?)/contexts/",session_str)
    if match:
        extracted_string=match.group(1)
        return extracted_string
    return ""
def get_str_from_food_dict(food_dict:dict):
    result=" , ".join([f'{int(value)} {key}' for key , value in food_dict.items()])
    return result

if __name__=="__main__":
    print(get_str_from_food_dict({'samosa':2, "dosa":9}))
    #print(extract_session_id("projects/chotu-chatbot-vo9u/agent/sessions/79ed/contexts/ongoing-order"))'''