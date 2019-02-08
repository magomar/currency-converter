# Currency Converter

Very simple flask app to perform currency conversion. It has been created just for learning purposes.

This app uses the free and open-source API provided by [Exchange Rates API](https://exchangeratesapi.io/), so there is no need for an api key.

## Requirements

It is recommended, although not mandatory, to use **`pipenv`** to install all dependencies, as it comes with a `Pipfile.lock` file.

## How to run

```shell
pipenv install
pipenv shell
flask run
```

Note: There is no need to export the environment variable FLASK_APP, since it is done automatically (thanks to the  `python-dotenv` package)