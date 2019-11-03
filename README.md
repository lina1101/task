#Hi!

This is a Django based implementation of the assignment.

##Running the server

The server can be run in 2 ways, feel free to run on alternate ports if needed.

###Docker

```shell script
docker build -t assignment -f Dockerfile .
docker run -p 8000:8000 assignment
```

The server is now accessible via `localhost:8000`

###Django server

This should work fine on any Linux distro and possibly Mac OS as well, though I cannot provide any guaratees.

Have a python 3.7 environment set up either via virtualenv (preferred) or natively and run the following commands.

```shell script
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver 8000
``` 

The server is now accessible via `localhost:8000`

##The server itself

Contains 4 pages, a root page + 1 page for each algorithm.

The root page at `/` contains a link to each of the algorithm pages.

Each algorithm page is rendered using Django templates and data validation is handled by Django Forms. Upon submitting data for processing the server will return both the result (if it was possible to calculate) and the execution time which is rendered at the bottom of the page.

The algorithm code can be found in `api/utils.py` with applicable documentation code where necessary. You will also find a testcase in `api/tests.py` though it is fairly bare-bones. Had there been a requirement for a more complex API I would have most likely introduced more test cases for any new endpoints.
