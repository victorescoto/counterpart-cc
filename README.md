# Counterpart Code Challenge

## First Run

To setup the project please run the following commands:
```
$ docker-compose up -d --build
$ docker-compose exec api python api/initial_data.py
```

## Following Runs

```
$ docker-compose up -d
```

After that you can access:
- http://localhost/ to access the aplication
- http://localhost:8000/docs to access the api docs

## What Technologies Were Used?

### Backend

- [FastApi](https://fastapi.tiangolo.com/)
- [Redis](https://redis.io/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [Postgres](https://www.postgresql.org/)

### Frontend

- [VueJS](https://vuejs.org/)
- [Bulma](https://bulma.io/)

## Next Steps

### Backend

- ~~Use a decorator to manage the cache for searches~~
- Use Alembic to handle the initial database setup and migrations
- Add unit tests

### Frontend

- Create the form to create the cities
- Show the search history
- Improve the layout overall
- Add unit tests
