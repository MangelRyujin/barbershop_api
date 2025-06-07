from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from apps.haircuts.routers import haircuts
from apps.gallery.routers import gallery
from apps.workers.routers import workers

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(haircuts.router, prefix="/haircuts", tags=["cuts"])
app.include_router(gallery.router, prefix="/gallery", tags=["gallery"])
app.include_router(workers.router, prefix="/workers", tags=["workers"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the Barber Shop API"}