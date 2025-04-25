
from random import randrange
from typing import Optional
from fastapi import FastAPI
from fastapi import Body
from pydantic import BaseModel

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool =True
    rating: Optional[int] = None

my_posts = [{"title":"Title of post 1", "content":"Content of post 1", "id":1}, 
            {"title":"Favourite foods", "content":"I like Pizza", "id":2},
            {"title":"Favourite Sport", "content":"I like WWE Wrestlemenia", "id":3}, 
            {"title":"Favourite Place", "content":"Dadar Siddhivinayak Ganpati bappa", "id":4}]

@app.get("/")
def root():
    return {"message": "Welcome to akash's api"}

#This is get function
@app.get("/posts_data")
def get_posts():
    return {"data":my_posts}

#This is post function
@app.post("/posts")
def create_posts(new_post: Post):
    post_dict = new_post.dict()
    post_dict['id'] = randrange(0, 1000000)
    my_posts.append(post_dict)
    return {"data":post_dict}

