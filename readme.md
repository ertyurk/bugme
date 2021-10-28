# BUGME - Bug orchestration tool

Disclaimer: Authenticator is working well but authorization is not inplemented yet. Please do not use in such environments that can effect you financially.

### Summary
This is a backend application implemented with FastAPI, Mongodb where you can create Users, Brands, Apps and report bugs and add Slack, Clickup integrations like [Shakebugs](https://www.shakebugs.com/) or [Instabug](https://instabug.com/)

Users can have multiple Brands (Users can be considered as Organizations too)
Brands can have multiple Apps 
For bug reporting, you need to use api key generated from brand (The Api key will be generated when you add a new brand automatically but also, you can generate a new one via `{API_URL}/api/v1/brands/get-api-key` with Brand ID param)
Client apps can report bugs along with Bundle ID and Platform and other details can be found in `{API_URL}/docs`. If the bundle ID is not saved, We create a new APP for that bundle ID along with correspondent Brand ID and User ID and platform information. 

In order to use this application, you need to create a Digitalocean spaces (or Aws S3 bucket) and MongoDB account.

## Developer setup 
- Makesure python version is 3.7 or more.
- Clone the repo.
    ```sh
    git clone https://github.com/ertyurk/bugme.git
    ```
- Go to project folder and Create a virtual environment.
    ```sh
    cd backend
    python3 -m venv .venv
    ```
- Activate virtual environment.
    ```sh
    chmod +x .venv/bin/activate
    source .venv/bin/activate
    ```
    - Deactivate if you need -> ```deactivate```
- Install dependencies.
    ```sh
    pip install -r requirements.txt
    ```
- Copy and update Environment variables with your mongo db url, table, secret key
    ```sh
    cp .env.sample .env
    ```
    - For secret key I use ```openssl rand -base64 128```
- Start the app with watcher to reload the app for each file change.
    ```sh
    uvicorn app.main:app --reload
    ```


## Docker setup

1. Clone this repo.
        
    ```
    git clone https://github.com/ertyurk/bugme.git
    ```
        
2. Update DNS config from CF or other domain provider.
3. Copy [`env.copy`](env.copy) to `.env` and Put desired credentials into `.env`.
4. Give permission to [`setup.sh`](setup.sh) and execute it for docker setup.

    ```
    chmod +X setup.sh
    ./setup.sh
    ```
5. To start server

    ```
    docker-compose -f docker-compose.prod.yml up -d --build
    ```

### Useful links

- Implemented with [FastAPI](https://fastapi.tiangolo.com/tutorial).
- [Docker cheat sheet](https://www.digitalocean.com/community/tutorials/how-to-remove-docker-images-containers-and-volumes#:~:text=Remove%20all%20images,docker%20images%20%2Da).
- [Traefik](https://doc.traefik.io/traefik/providers/docker/) used for dockerized proxy setup.
- [MongoDB Atlas](https://docs.atlas.mongodb.com/tutorial/deploy-free-tier-cluster/)
