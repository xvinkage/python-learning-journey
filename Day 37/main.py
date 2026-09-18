import requests
from dotenv import load_dotenv
import os
import datetime


load_dotenv()

TOKEN = os.getenv("TOKEN")
USERNAME = os.getenv("USERNAME")


pixela_url = "https://pixe.la/v1/users"
pixela_endpoint = f"{pixela_url}/{USERNAME}/graphs"

user_params= {"token": TOKEN,
              "username": USERNAME,
              "agreeTermsOfService": "yes",
              "notMinor": "yes"


}

# print(response.text)
# response = requests.post(url=pixela_url)

graph_config = {
    "id": "graph1",
    "name": "my coding graph",
    "unit": "days",
    "type": "int",
    "color": "momiji"
}
headers = {
    "X-USER-TOKEN": TOKEN
    }
# response2 = requests.post(url=pixela_endpoint, json=graph_config,  headers=headers)
# print(response2.text)

today = datetime.date.today().strftime("%Y%m%d")
pixel_endpoint = f"{pixela_endpoint}/graph1/{today}"

graph_paramas = {"date": today,
                 "quantity": input("How much did you code today?")
                 }
response3 = requests.put(url=pixel_endpoint, headers=headers, json=graph_paramas)
print(response3.text)