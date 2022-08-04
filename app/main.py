import sys
import os

sys.path.append(os.getcwd())
import uvicorn

from app.endpoints.app import create_app
from app.models.user import Base as B0
from app.models.product import Base as B1
from app.models.sells import Base as B2
from app.database.database import DataBase

app = create_app()
# Crear estructura básica de modelos en base datos
db = DataBase()
B0.metadata.create_all(db.engine)
B1.metadata.create_all(db.engine)
B2.metadata.create_all(db.engine)
db.session.close()

if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=5001, reload=True)

