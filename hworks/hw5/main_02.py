from enum import Enum

import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

movies = []


class Genre(Enum):
    THRILLER = "боевик",
    FANTASY = "фантастика",
    COMEDY = "комедия"


class Movie(BaseModel):
    id: int
    title: str
    description: str
    genre: str


class MovieIn(BaseModel):
    title: str
    description: str
    genre: str


@app.get("/movies/{genre}", response_model=list[Movie])
async def get_movies(genre: str):
    result = []
    for movie in movies:
        if movie.genre == genre:
            result.append(movie)
    return result


@app.post("/movies/", response_model=Movie)
async def create_movies(new_movie: MovieIn):
    movies.append(Movie(id=len(movies) + 1,
                        title=new_movie.title,
                        description=new_movie.description,
                        genre=new_movie.genre))
    return movies[-1]


if __name__ == '__main__':
    uvicorn.run(
        "main_02:app",
        host="127.0.0.1",
        port=8000,
        reload=True
    )
