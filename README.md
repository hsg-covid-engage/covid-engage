# Covid Symptom Tracker

The Covid Symptom Tracker is a web application that allows COVID-19 Positive patients to tracke their symptoms while they are sick. The tracker aims to provide researchers with a better insight into the progression of COVID19 across a population.

## Installation

### Heroku one Click
[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/hsg-covid-engage/covid-engage/tree/docker-composed-app)

### Docker

### Vanilla

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