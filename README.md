The code of http://www.policyinsights.us/

## Local deployment

[Install python3](https://www.python.org/downloads/).

### Create virtualenv and install requirements

https://packaging.python.org/guides/installing-using-pip-and-virtualenv/

On Windows:

```
pip install --upgrade pip
pip install --user virtualenv
virtualenv env
.\env\Scripts\activate
pip install -r requirements.txt
```

### Start development server

```
python manage.py migrate
python manage.py loaddata news
python manage.py runserver
```

Open browser at

http://127.0.0.1:8000/
