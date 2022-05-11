import requests
import json

def get_data(id=None):
    data={"id":id}
    json_data=json.dumps(data)
    URL="http://127.0.0.1:8000/stu/"
    req=requests.get(url=URL,data=json_data)
    res=req.json()
    print(res)


#get_data(1)


def post_data():
    data={
    "name":"shital529",
    "roll_no":50,
    "city":"PUNE"
    }
    json_data=json.dumps(data)
    URL="http://127.0.0.1:8000/stu/"
    req=requests.post(url=URL,data=json_data)
    res=req.json()
    print(res)
#post_data()

def update_data():
    data={'id':4,
    "name":"swap123",
    "roll_no":67,
    "city":"Ahmednager"
    }
    json_data=json.dumps(data)
    URL="http://127.0.0.1:8000/stu/"
    req=requests.put(url=URL,data=json_data)
    res=req.json()
    print(res)
#update_data()

def delete_data():
    id=4
    data={"id":id}
    json_data=json.dumps(data)
    URL="http://127.0.0.1:8000/stu/"
    req=requests.delete(url=URL,data=json_data)
    res=req.json()
    print(res)
delete_data()
