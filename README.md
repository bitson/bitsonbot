### Clonar el repositorio

```
git clone git@github.com:bitson/bitsonbot.git
```
o 
```
git clone https://github.com/bitson/bitsonbot.git
```
 
### crear el entorno virtual ([virtualenvwrapper](http://virtualenvwrapper.readthedocs.io/en/latest/install.html "virtualenvwrapper"))

```
mkvirtualenv -p $(which python3) bitsonbot
```

### Instalamos los requirements.

```
cd bitsonbot
pip install -r requirements.txt
```

### Creamos la base de datos ([docker](https://docs.docker.com/engine/installation/ "docker"))

```
docker run --name bitsonbot -e POSTGRES_PASSWORD=bitson -e POSTGRES_USER=bitsonbot -e POSTGRES_DB=bitsonbot -p 5432:5432 -d postgres
```

### [Hacemos el upgrade de la base](https://github.com/bitson/bitsonbot/wiki/Base-de-datos-y-migraciones/ "")

```
PYTHONPATH=. alembic upgrade head
``` 

### Corremos el bot

```
./run.py TOKEN
```
