from app.endpoints import login_user_endpoint 


from app.endpoints import (
    ##Users
    create_user_endpoint,
    get_user_id_endpoint,
    get_user_id_clean_endpoint,
    get_all_users_endpoint,
    get_all_users_clean_endpoint,
    get_all_active_users_endpoint,
    change_user_password_endpoint,
    update_user_data_endpoint,
    activate_user_endpoint,
    deactivate_user_endpoint,
    update_user_role_endpoint,
    update_user_status_endpoint,
    ##Enrollment
    create_enrollment_endpoint,
    ##Products
    create_product_endpoint,
    get_all_products_endpoint,
    get_product_name_endpoint,
    get_product_tag_endpoint,
    get_product_branch_endpoint,
    update_product_data_endpoint,
    update_product_amount_endpoint,
    get_product_id_endpoint,
    ##Company
    create_company_endpoint,
    get_company_name_endpoint,
    
    ##Sells
    create_sell_endpoint,
)

from dotenv import load_dotenv
from fastapi import FastAPI
from app.models.user import Base as B0
from app.models.product import Base as B1
from app.models.sells import Base as B2
from app.database.database import DataBase
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
load_dotenv()

def create_app():
    app = FastAPI()
    ##Users

    # Crear estructura básica de modelos en base datos
    db = DataBase()

    B0.metadata.create_all(db.engine)
    B1.metadata.create_all(db.engine)
    B2.metadata.create_all(db.engine)
    app.include_router(login_user_endpoint.router)
    app.include_router(create_user_endpoint.router)
    app.include_router(get_user_id_endpoint.router)
    app.include_router(get_user_id_clean_endpoint.router) 
    app.include_router(get_all_users_endpoint.router) 
    app.include_router(get_all_users_clean_endpoint.router)
    app.include_router(get_all_active_users_endpoint.router) 
    app.include_router(change_user_password_endpoint.router)
    app.include_router(update_user_data_endpoint.router)
    app.include_router(activate_user_endpoint.router)
    app.include_router(deactivate_user_endpoint.router)
    app.include_router(update_user_role_endpoint.router)
    app.include_router(update_user_status_endpoint.router)
    ##Enrollment
    app.include_router(create_enrollment_endpoint.router)
    ##Products
    app.include_router(create_product_endpoint.router)
    app.include_router(get_product_id_endpoint.router)
    app.include_router(get_all_products_endpoint.router)
    app.include_router(get_product_name_endpoint.router)
    app.include_router(get_product_branch_endpoint.router)
    app.include_router(get_product_tag_endpoint.router)
    app.include_router(update_product_data_endpoint.router)
    app.include_router(update_product_amount_endpoint.router)
    ##Company
    app.include_router(create_company_endpoint.router)
    app.include_router(get_company_name_endpoint.router)
    ##Sells
    app.include_router(create_sell_endpoint.router)
    return app