# Sample Astra DB FastAPI app

This minimal API illustrates a good pattern to integrate Astra DB
as the backing storage for your FastAPI applications.

You can run it yourself by following the instructions given below
or just use it as a reference when writing your own API.

### Setup

First make sure you have an [Astra DB instance](https://awesome-astra.github.io/docs/pages/astra/create-instance/)
up and running.
Have the ["Token"](https://awesome-astra.github.io/docs/pages/astra/create-token/)
and the ["secure connect bundle"](https://awesome-astra.github.io/docs/pages/astra/download-scb/) zipfile
ready
(see the links for more details).

Make the secrets and the connection details available by copying
the `.env.sample` file to a new `.env` and customizing it. This
will be picked up by the API on startup (no need to `source` the
file thanks to the `python-dotenv` utility).

Next you need some Python dependencies. Preferrably in a virtual environment,
run the following:

```
pip install -r requirements.txt
```

> Please stick to Python version 3.7 or higher.

Your Astra DB instance is brand new: in order to create the
table needed by the API and populate it with a few sample rows,
you can simply launch the provided initialization script once:
```
python storage/db_initialize.py
```

> This step, which will also serve as test of the connection to Astra DB,
> has the sole purpose of making this demo application self-contained:
> in a production setup, you'll probably want to
> handle schema changes in a more controlled way.

### Run and test the API

You're ready to go: start the API with

```
uvicorn api:app
```

and, in a separate console, you can test the endpoints with the following
`curl` commands:

```
curl -s \
  localhost:8000/animal/Vanessa/atalanta \
  -H 'Content-Type: application/json' \
  | jq

curl -s \
  localhost:8000/animal/Vanessa \
  -H 'Content-Type: application/json' \
  | jq

curl -s -X POST \
  localhost:8000/animal \
  -d '{"genus":"Philaeus", "species":"chrysops", "image_url":"https://imgur.com/F66x0Pt", "size_cm":0.12, "sightings":2, "taxonomy": ["Arthropoda","Arachnida","Aranea","Salticidae"]}' \
  -H 'Content-Type: application/json' \
  | jq

curl -s \
  localhost:8000/plant/Plantago \
  -H 'Content-Type: application/json' \
  | jq
# by trying with `curl -i -s ...` and no jq piping one can
# see that this has "Transfer-Encoding: chunked".
```

### Remarks

The database session is handled as a process-wide singleton
using a global cache, as per best practices with the Cassandra driver.

Likewise, to optimize performance, a global cache of prepared statement
is used throughout the API (more precisely, there is one such cache per each FastAPI worker process).

Finally, here FastAPI's dependency mechanisms are used to provide the database
session to all endpoints that need it (the `Depends(...)` argument
to the endpoint functions). Note that an async function `yield`ing the session
is introduced to comply with the function (async generator) expected by
`Depends`.

Streaming (coming soon).

### See also
