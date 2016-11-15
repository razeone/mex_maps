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

#### Intro
mex_maps is a django-based API which allows users to perform GeoSpatial analysis, and retrieve geographic data.

This is project is going to be a set of geographic APIs for general purpose, it's inspired by the beautiful maps and APIs from [diegovalle](https://github.com/diegovalle),
particulary from [this repo](https://github.com/diegovalle/hoyodecrimen.api)

#### Installation
You need some tools installed in your system in order to run this application:

* [PostgreSQL](http://postgresql.org/)
* [PostGIS](http://www.postgis.net/)
* [Python 3.5+](https://www.python.org/)
* [Virtualenv](https://virtualenv.pypa.io/en/stable/)
* GEOS
* GDAL
* [pip](https://pypi.python.org/pypi/pip)

There's also a [tutorial](https://docs.djangoproject.com/es/1.10/ref/contrib/gis/tutorial/) on installing and running GeoDjango,
which is actually the base of this development.

###### Setting up environment

After you install everything, you need to create a virtualenv and install requirements via pip:
```
$ virtualenv -p python3.5 env
$ source env/bin/activate
$ pip install -r requirements.txt
```

Then you can edit the `environ.rc` file with your data and then load variables:

```
$ source environ.rc
```

###### Setting up database

You need to create a database with postgis support:

```
$ createdb mex_maps -E UTF-8
$ psql -d mex_maps
# create extension postgis
```

Create the database
```
$ cd world
$ ./manage.py makemigrations
$ ./manage.py migrate
```

And now you can load the example data ziped in the `world/data` directory:
```
$ ./manage.py shell
>>> from world.load import run
>>> run()
```

You'll see a list of the countries created in your database

And you can now browse the API at `http://localhost:8000`

###### Testing

```
$ ./manage.py test
```