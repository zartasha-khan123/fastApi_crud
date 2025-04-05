
#------------------------------------------------GET- fetch (Fastapi)-------------------------------------------------------
# FastAPI se import kar rahe hain, taaki hum API bana sakein ---  fastapi is a class also
from fastapi import FastAPI

from pydantic import BaseModel # Yeh ek library hai jo data validation aur serialization ke liye use hoti hai
# Yeh ek class hai jo FastAPI ko define karne ke liye use hoti hai

# FastAPI ka ek instance bana rahe hain
app = FastAPI() 

names = ["Ali", "Ahmed", "Sara","zubair","dania"] # Yeh ek list hai jisme kuch naam hain

# Yeh ek GET request ka endpoint define kar raha hai jo root ("/") pe chalega
#@app is a decorator jo function ko FastAPI ka route banata hai
# Yeh function jab bhi root URL pe request aayegi, tab chalega
@app.get("/")   #url
def get_function():  #jab url call huga tw ye function khud say chalinga
    return  names  #ye function ak json response return kr raha hain



#---------------------------------------POST(Create)fast api----------------------------------------------------

class Data_post(BaseModel): #ye class pydantic ki baseModel se inherit kar rahi hai
    name: str #ye variable string type ka hai
   


@app.post("/") #url

def post_function(data: Data_post):
    #ye function jab bhi /fastapi_data URL pe request aayegi, tab chalega
    names.append(data.name)
    
    return names #ye function ak json response return kr raha hain
    # return {"name":f" My name is {data.name}", #ye data variable se name le raha hai
    #         "age":f" my age is {data.age}",
    #         "city":f"my city name is {data.city}"}   #ye function ak json response return kr raha hain
    
    
 #---------------------------------------Delete(delete)fast api----------------------------------------------------
   
    
@app.delete("/{name}") # url

def delete_function(name : str):
    names.remove(name)
    return names #ye function ak json response return kr raha hain
    
    
#---------------------------------------PUT(update)fast api----------------------------------------------------

@app.put("/{name}") #url

def put_delete(name:str , data:Data_post): #ye function jab bhi /fastapi_data URL pe request aayegi, tab chalega
    for i , n in enumerate(names): #ye loop list ke har element ko check kar raha hai
       if n == name:
        names[i] = data.name #ye naam ko update kar raha hai
    return names #ye function ak json response return kr raha hain
