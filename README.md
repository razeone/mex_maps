# mex_maps
Let's map México and see what happens

#### Quickstart

```
$ export DATABASE_NAME='your_geographic_db'
$ export DATABASE_USER='your_db_user'
$ export DATABASE_PASSWORD='your_db_password'
$ ./manage.py makemigrations
$ ./manage.py migrate
$ unzip world/data/TM_WORLD_BORDERS-0.3.zip
$ ./manage.py shell
>>> from world import load
>>> load.run()
$ ./manage.py createsuperuser
$ ./manage.py runserver
```
