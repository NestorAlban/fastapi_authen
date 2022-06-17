import sys
import os

sys.path.append(os.getcwd())
import uvicorn

from app.endpoints.app import create_app
from app.models.user import Base
from app.database.database import DataBase

app = create_app()
# Crear estructura básica de modelos en base datos
db = DataBase()
Base.metadata.create_all(db.engine)
db.session.close()

if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=5001, reload=True)

