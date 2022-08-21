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
5. Run Docker file
    - Create image
        ```shell
        docker build -t python-fast .
        ´´´
    - Run image and server
        ```shell
        docker run -p 8000:8000 python-fast
        ´´´
6. App Flow
    Folder database
    Folder services
    Folder usercase
    Folder endpoints 

7. Run Docker
    - Create image
        ```shell
            sudo docker-compose up
        ´´´
    - Remove db data
        ```shell
            sudo remove -r -f postgres-data
        ´´´

create new virtualenv with pyenv

- pyenv virtualenv <python version> <folder/project name>
- pyenv local <folder/project name>

install inside the virtualenv
- pithon -m pip install <library name>