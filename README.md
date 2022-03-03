# livlearn api 

This was the backend of the livlearn web app which I built to streamline the collecting, sharing and curating of online learning content, including books, videos, blogs, courses and podcasts. It is based on Django Rest Framework. livlearn is no longer deployed anywhere. I may redeploy it if there is significant interest from anyone. The web app also used Firebase alongside the api to enable real time editing in the drag and drop list editor.

# Original deployment plan

When it was live, this api was deployed on a Digital Ocean server with Dokku (https://dokku.com/) which ended up being a cheap and reasonably straightforward alternative to Heroku. 

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

 Also if needed at the start run
 ```
python manage.py createsuperuser
```
