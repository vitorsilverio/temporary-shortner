# temporary-shortner
A webapp that shortens URLs but for a limited time

## Demo site
[https://temporary-shortner.herokuapp.com/](https://temporary-shortner.herokuapp.com/)

## Instalation
### Using docker
```
docker build -t tshort .
docker run -d --name tshort -p{PORT}:80 -e REDIS_URL="{REDIS_URL" -e APP_BASE_URL="{BASE_URL}" tshort
```
### Using docker-compose
1. Rename `docker-compose.yml.example` to `docker-compose.yml`
2. Modify `docker-compose.yml` to reflect your configuration
3. Run `docker-compose up -d`

### Locally with uvicorn
1. Create a python virtualenv (At least python 3.9)
2. Install dependencies with `pip install -r requirements.txt`
3. Run uvicorn `python -m uvicorn app.main:app --host 0.0.0.0 --port 8080 --reload`

## Options
The folowing enviroments variable configure the app

Variable|Default|Description
---|-------|-----------
APP_BASE_URL|http://localhost:5000|Url base for the shortened link
REDIS_URL|redis://localhost|Url for Redis
EXPIRATION_TIME|604800|Time that link expires in redis(Default 7 days)

## Contributing
You can make a fork and submit Pull Requests with new features, report issues or [Buy me a ☕](https://www.buymeacoffee.com/vitorsilverio)
