#YAJAT
import os
import requests

def linkedin(linkedin_profile_url:str):
    api_endpoint = "https://nubela.co/proxycurl/api/v2/linkedin"
    headers = {'Authorization': 'Bearer ' + os.environ.get("PROXYCURL_API_KEY")}

    response= requests.get(api_endpoint,params={"url":linkedin_profile_url},headers=headers)
    data=response.json()
    data = {
        x: y
        for x, y in data.items()
        if y not in ["people also viewed", "certifications"]
    }
    if data.get("groups"):
        for group_dict in data.get("groups"):
            group_dict.pop("profile_pic_url")

    return data