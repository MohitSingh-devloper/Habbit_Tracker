from _datetime import datetime
import requests
pixela_endpoint="https://pixe.la/v1/users"
USERNAME="mohitsingh"
TOKEN="hudbsdberfgrep"
GRAPH_ID="graph1"

user_prams={
    "token":"hudbsdberfgrep",
    "username":"mohitsingh",
    "agreeTermsOfService":"yes",
    "notMinor":"yes"
}

#CREATING USER ACCOUNT ON THE PIXELA

# response=requests.post(pixela_endpoint,json=user_prams)
# print(response.text)

graph_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs"
graph_param={
    "id":GRAPH_ID,
    "name":"Coding Graph",
    "unit":"minutes",
    "type":"float",
    "color":"ajisai"

}

header={
    "X-USER-TOKEN":TOKEN
}

#ADDING GRAPH AT USERID:
# response=requests.post(url=graph_endpoint,json=graph_param,headers=header)
# print(response.text)


#ADDING THE PIXEL AT THE GRAPH

pixel_add_endpoint=f"{graph_endpoint}/{GRAPH_ID}"
today=datetime(year=2021,month=12,day=25)
add_pixel_param={
    "date":today.strftime("%Y%m%d"),
    "quantity":"90"
}

# response=requests.post(url=pixel_add_endpoint,json=add_pixel_param,headers=header)
# print(response.text)

#UPDATING DATA WITH THE PUT() METHOD:
update_endpoint=f"{graph_endpoint}/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

new_pixel_data={
    "quantity":"40"
}

# response=requests.put(url=update_endpoint,json=new_pixel_data,headers=header)
# print(response.text)

#DELETING DATA WITH THE DELETE() METHOD:
# delete_endpoint=f"{graph_endpoint}/{GRAPH_ID}/{}"
# response=requests.delete(url=delete_endpoint,headers=header)
# print(response.text)