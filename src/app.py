from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .api.endpoints import haircuts

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(haircuts.router)
# app.include_router(gallery.router)
# app.include_router(workers.router)
# app.include_router(reservations.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Barber Shop API"}