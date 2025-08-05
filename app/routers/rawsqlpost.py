from .. import schemas
from fastapi import FastAPI, Response, status, HTTPException, APIRouter
import psycopg2
from psycopg2.extras import RealDictCursor
import time

router = APIRouter(
    tags=["Raw SQL Posts"]  # Tags for the router
)

# Connect to the PostgreSQL database and Use psycopg2 to connect and execute raw SQL queries
while True:
    try:
        conn = psycopg2.connect(
            host='localhost',
            database='fastapi',
            user='postgres',
            password='Sakshi@2004',
            cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print("Database connection successful")
        break
    except Exception as e:
        print("Database connection failed")
        print(f"Error: {e}")
        time.sleep(2)

# raw SQL queries
my_posts = [{'title': 'Title of post 1', 'content': 'Content of post 1', 'id': 1}, {
    'title': 'Favourite Food', 'content': 'Biryani', 'id': 2}]


@router.get("/posts")
def getpost():
    cursor.execute("""SELECT * FROM posts""")
    posts = cursor.fetchall()
    if not posts:   # If no posts are found in the database
        return {"data": "No posts available"}
    print(posts)
    return {"data": my_posts}


@router.post("/posts", status_code=status.HTTP_201_CREATED)
def createposts(post: schemas.CreatePost):
    cursor.execute("""INSERT INTO posts(title, content, published) VALUES (%s, %s, %s) RETURNING *""",
                   (post.title, post.content, post.published))
    new_post = cursor.fetchone()  # convert pydantic model to dict
    conn.commit()
    return {"data": new_post}


# put before /posts/{id} to avoid conflict, {id} is a variable, hence latest canbe taken for a variable and passed there if not written early
@router.get("/posts/latest")
def get_latest_post():
    if my_posts:
        # -1 returns the last element in the list
        return {"data": my_posts[-1]}
    return {"data": "No posts available"}


@router.get("/posts/{id}")
def get_post(id: int):
    cursor.execute("""SELECT * FROM posts WHERE id = %s""", (str(id),))
    post = cursor.fetchone()  # fetch one post by id
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Post with id {id} not found')
    return {'post detail': post}


@router.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
    cursor.execute(
        """DELETE FROM posts WHERE id = %s RETURNING *""", (str(id),))
    deleted_post = cursor.fetchone()
    conn.commit()
    if deleted_post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Post with id {id} not found')
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.put("/posts/{id}")
def update_post(id: int, post: schemas.UpdatePost):

    cursor.execute("""UPDATE posts SET title = %s, content = %s, published = %s WHERE id = %s RETURNING *""",
                   (post.title, post.content, post.published, str(id)))
    updated_post = cursor.fetchone()
    conn.commit()
    if updated_post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Post with id {id} not found')
    return {"data": updated_post}
