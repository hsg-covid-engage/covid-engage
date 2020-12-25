# Covid Symptom Tracker

The Covid Symptom Tracker is a web application that allows COVID-19 Positive patients to tracke their symptoms while they are sick. The tracker aims to provide researchers with a better insight into the progression of COVID19 across a population.

## Installation

### 1 Heroku one Click
[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/hsg-covid-engage/covid-engage/tree/main)

### 2 Docker Compose

Run the following

```bash
docker-compose build
docker-compose up -d
```

### 3 Vanilla (full)

#### Flask app 

Install Postgresql (anything above Postgres 9 should work). [Here](https://www.postgresql.org/docs/12/installation.html) is a tutorial for Postgres 12

Create a Postgres Username, password. Add the connection url into your environment, i.e.

```
export DATABASE_URL=postgresql://user:password@localhost:5432/database_name
```

Set up the Flask Application. Flask will automatically configure the database from the configuration in the `models` folder
```bash
# create virtual environment & activate
python3 -m venv venv
. venv/bin/activate

# install requirements
pip install -r requirements.txt

# run the app
gunicorn --bind 0.0.0.0:5000 wsgi:app
```

**Note* installing `psycopg2-binary` might fail on OSX. You might need to do the following
1. Make sure postgresql is installed `brew install postgresql`
2. Set the openssl to venv environment variable as per [this StackOverflow answer](https://stackoverflow.com/a/55839410)
```export LDFLAGS="-L/usr/local/opt/openssl/lib"```

## Usage
Deploy it on a web server and send the sign up link to your patients so they can get started.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)