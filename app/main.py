import sys
import os

sys.path.append(os.getcwd())
import uvicorn

from fastapi.middleware.cors import CORSMiddleware

from app.database import (
    LIVE_SERVER, 
    LIVE_SERVER_2, 
    LIVE_SERVER_3, 
    LOCAL_HOST, 
    LOCAL_HOST2
)
from app.endpoints.app import create_app
from app.models.user import Base as B0
from app.models.product import Base as B1
from app.models.sells import Base as B2

app = create_app()

origins = [LIVE_SERVER, LIVE_SERVER_2, LIVE_SERVER_3, LOCAL_HOST, LOCAL_HOST2]

app.add_middleware(
    CORSMiddleware, 
    allow_origins = origins, 
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"],
)

if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=5432, reload=True)

