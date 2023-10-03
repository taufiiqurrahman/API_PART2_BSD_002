# from fastapi import FastAPI, Request

# app = FastAPI()

# @app.get("/example")
# def read_example_headers(request: Request):
#     headers = request.headers
#     # Access specific header values
#     user_agent = headers.get("user-agent")
#     authorization = headers.get("authorization")
#     custom_header = headers.get("custom-header")

#     return {
#         "User-Agent": user_agent,
#         "Authorization": authorization,
#         "Custom-Header": custom_header
#     }

# from fastapi import FastAPI, Response

# app = FastAPI()

# @app.get("/example")
# def example_endpoint():
#     content = "Hello, this is the response content."

#     # Create a Response object and set custom headers
#     response = Response(content=content)
#     response.headers["X-Custom-Header"] = "This is custom value"
#     response.headers["Authorization"] = "pass_token_1234"

#     return response


from fastapi import FastAPI, HTTPException, Header

app = FastAPI()

API_KEY = "testingapitokenkey1234" #testing api token key 1234

@app.get("/")
def home():
  return {"message":"This is my API. Welcome!"}

@app.get("/protected")
def protect(api_key: str = Header(None)):

  if api_key is None or api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key")

  return {"message":"This endpoint is protected by API Token Key.",
          "data":{"1":{"username":"fahmi","password":"1234"},
                  "2":{"username":"raka","password":"abcd123"},
                  "3":{"username":"rachman","password":"h8teacher"}
                 }
          }

from fastapi import FastAPI, HTTPException, Header

app = FastAPI()

API_KEY = "phase0h8"

data = {"name":"shopping cart",
        "columns":["prod_name","price","num_items"],
        "items":{}}

@app.get("/")
def root():
    return {"message":"Welcome to Toko H8 Shopping Cart! There are some features that you can explore",
            "menu":{1:"See shopping cart (/data)",
                    2:"Add item (/add) - You may need request",
                    3:"Edit shopping cart (/edit/id)",
                    4:"Delete item from shopping cart (/del/id)"}}

@app.get("/cart")
def show():
    return data

@app.post("/add")
def add_item(added_item:dict, api_key: str = Header(None)):
    if api_key is None or api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key. You are not allowed to add data!")
    else:
        id = len(data["items"].keys())+1
        data["items"][id] = added_item
        return f"Item successfully added into your cart with ID {id}"

@app.put("/edit/{id}")
def update_cart(id:int,updated_cart:dict, api_key: str = Header(None)):
    if id not in data['items'].keys():
        raise HTTPException(status_code=404, detail=f"Item with ID {id} not found")
    else:
        if api_key is None or api_key != API_KEY:
            raise HTTPException(status_code=401, detail="Invalid API Key. You are not allowed to edit data!")
        else:
            data["items"][id].update(updated_cart)
            return {"message": f"Item with ID {id} has been updated successfully."}

@app.delete("/del/{id}")
def remove_row(id:int, api_key: str = Header(None)):
    if id not in data['items'].keys():
        raise HTTPException(status_code=404, detail=f"Item with ID {id} not found")
    else:
        if api_key is None or api_key != API_KEY:
            raise HTTPException(status_code=401, detail="Invalid API Key. You are not allowed to delete data!")
        else:
            data["items"].pop(id)
            return {"message": f"Item with ID {id} has been deleted successfully."}