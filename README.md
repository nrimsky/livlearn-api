# livlearn api 

https://api.livlearn.howshouldilearn.com/

## pushing to remote git repo

```
git push origin master
```

## pushing to production (dokku on digital ocean)

Set `DEBUG=False` in `livlearn/settings.py`
```
git push dokku master
```

## running locally

Set `DEBUG=True` in `livlearn/settings.py`
```
python manage.py migrate api
python manage.py makemigrations
python manage.py runserver
```
