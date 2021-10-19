# Overview

This repository demonstrates some minimal examples of using database interaction techniques that we want to migrate towards.

 1. Async support in [SQLAlchemy 1.4](https://docs.sqlalchemy.org/en/14/orm/extensions/asyncio.html)
 2. Using [sqlmodel](https://github.com/tiangolo/sqlmodel) to combine SQLAlchemy and Pydantic models
 3. Using [cockroachdb](https://www.cockroachlabs.com/) 


# Run

Clone this repository, and `docker-compose up -d`.  Look at `docker-compose logs jupyter` to find the url with auth token, which will look something like `http://127.0.0.1:8888/?token=508e0e0761f05436685b67c9233104b65e8061eea213a75a`.

Once you have Jupyter open, navigate to the `notebooks` folder and explore the four Notebooks and two flat `.py` files.  `sa_models.py` is a traditional SQLAlchemy implementation of a `User` and `Message` model.  `models.py` contains a `sqlmodel` equivalent, and that is what is used in the Notebooks.

The Notebooks demonstrate how to add and query data synchronously and asynchronously against Postgres and CockroachDB.  

# Cockroach async blocker

So far I have not been able to connect and interact with Cockroach using an async engine.

Related tickets:
 * https://github.com/cockroachdb/sqlalchemy-cockroachdb/issues/165
 * https://github.com/cockroachdb/cockroach/issues/70209