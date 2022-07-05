from app.endpoints import login_user_endpoint 


from app.endpoints import (
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
    create_product_endpoint
)

from dotenv import load_dotenv
from fastapi import FastAPI

load_dotenv()

def create_app():
    app = FastAPI()
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
    app.include_router(create_product_endpoint.router)
    return app