import sys
import os

sys.path.append(os.getcwd())
import uvicorn


from app.endpoints.app import create_app
from app.models.user import Base as B0
from app.models.product import Base as B1
from app.models.sells import Base as B2

app = create_app()

if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=5432, reload=True)

