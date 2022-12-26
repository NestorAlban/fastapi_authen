#asd
1. Run fastapi
    - Run with uvicorn
        ```shell
        python -m uvicorn app.main:app --reload
        ```
2. Save requirements.txt
    ```shell
    pip --disable-pip-version-check list --format=freeze >requirements.txt
    ´´´
3. Install packages with pip
#
4. Install packages with poetry
#
5. .env data
    Variables needed to configure in the environment .env file
    - User is the user configured in the database administrator
    - Password is the password configured in the database administrator
    - Host is localhost by default, just use the service name if docker compose is used
    - Port is 5432 or the configured port in the database administrator
    - Name is the name of the server created


6. App Flow
    Folder database
    Folder services
    Folder usercase
    Folder endpoints 

7. Docker
    - Configure Docker-compose file
            The host of the .env has to change from localhost or 8080 to sellsdb, 
        the name of the service in the doc.com. file
            Set the same network in the services that are going to be used
    - Create image
        ```shell
            sudo docker-compose up
        ´´´
    - Shutdown the image
        ```shell
            sudo docker-compose down
        ´´´
    - Remove db data
        ```shell
            sudo rm -r -f postgres-data/
        ´´´

8. Build up the Front-end
    - Install node and start npm for the page folder.
    - Create a origin.py file in database folder and put the links that want to use as for front-end, those like "http://localhost" or "http://localhost:8080", that will let those links to be accepted by FastAPI CORS.


create new virtualenv with pyenv

- pyenv virtualenv <python version> <folder/project name>
- pyenv local <folder/project name>

install inside the virtualenv
- pithon -m pip install <library name>