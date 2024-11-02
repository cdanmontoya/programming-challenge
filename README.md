# Python Template

![](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![](https://img.shields.io/badge/fastapi-109989?style=for-the-badge&logo=FASTAPI&logoColor=white)
![](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)
![](https://img.shields.io/badge/rabbitmq-%23FF6600.svg?&style=for-the-badge&logo=rabbitmq&logoColor=white)
![](https://img.shields.io/badge/GitHub_Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg?style=for-the-badge)](https://github.com/psf/black)

[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=cdanmontoya_python-template&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=cdanmontoya_python-template)
[![Bugs](https://sonarcloud.io/api/project_badges/measure?project=cdanmontoya_python-template&metric=bugs)](https://sonarcloud.io/summary/new_code?id=cdanmontoya_python-template)
[![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=cdanmontoya_python-template&metric=code_smells)](https://sonarcloud.io/summary/new_code?id=cdanmontoya_python-template)
[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=cdanmontoya_python-template&metric=coverage)](https://sonarcloud.io/summary/new_code?id=cdanmontoya_python-template)
[![Duplicated Lines (%)](https://sonarcloud.io/api/project_badges/measure?project=cdanmontoya_python-template&metric=duplicated_lines_density)](https://sonarcloud.io/summary/new_code?id=cdanmontoya_python-template)
[![Lines of Code](https://sonarcloud.io/api/project_badges/measure?project=cdanmontoya_python-template&metric=ncloc)](https://sonarcloud.io/summary/new_code?id=cdanmontoya_python-template)
[![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=cdanmontoya_python-template&metric=reliability_rating)](https://sonarcloud.io/summary/new_code?id=cdanmontoya_python-template)
[![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=cdanmontoya_python-template&metric=security_rating)](https://sonarcloud.io/summary/new_code?id=cdanmontoya_python-template)
[![Technical Debt](https://sonarcloud.io/api/project_badges/measure?project=cdanmontoya_python-template&metric=sqale_index)](https://sonarcloud.io/summary/new_code?id=cdanmontoya_python-template)
[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=cdanmontoya_python-template&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=cdanmontoya_python-template)
[![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=cdanmontoya_python-template&metric=vulnerabilities)](https://sonarcloud.io/summary/new_code?id=cdanmontoya_python-template)


# Folder structure
The folder structure is inspired in a Hexagonal Architecture and borrows concepts from Domain Driven Design. The main 
goal is to achieve a decoupled implementation that keeps the business knowledge and processes defined in entities,
abstractions and services in the `domain` and `app` packages, and the concrete implementations and details that depend on external systems or third-party 
software in the `infrastructure` package.

```text
.
├── src/
│   ├── app/                        # Defines the application behavior
│   │   ├── commands/                   # Holds the data required to execute operations that write into the system
│   │   ├── queries/                    # Holds the data required to execute operations that read data from the system
│   │   ├── use_cases/                  # Implements the business logic
│   │   └── ports/                      # Defines abstractions to interact with external systems
│   │       └── output/                  
│   ├── domain/                     # Represents the business knowledge and understanding
│   │   ├── model/                      # Defines relevant business entities and their operations
│   │   ├── services/                   # Implements logic that involves several entities
│   │   └── events/                     # Holds information about the facts that happened on the system
│   └── infrastructure/
│       ├── acl/                    # Anti corruption layer that aims to keep the domain isolated from external systems
│       │   ├── dto/                    # Data transfer objects for both input and output
│       │   └── translators/            # Translates DTOs into commands, queries and domain entities, and vice-versa
│       ├── adapters/               # Concrete implementations depending on frameworks and particular technologies
│       │   ├── input/                  # Input adapters that receive interactions from external systems using different protocols
│       │   │   ├── events/
│       │   │   └── http/
│       │   └── output/                 # Output adapters that call external systems
│       ├── injector/               # Dependency injection configuration
│       └── migrations/             # Database schema evolutions configuration
└── test/
    ├── unit/
    │   └── ...                     # Both unit and integration tests mimic the same folder structure as the src/ folder, but only for the required files
    ├── it/
    │   └── ...
    └── resources/
        └── factories/              # Factories to generate domain-compliant data
    └── conftest.py                 # Useful fixtures for easier testing
```

This folder structure is enforced using [import-linter](https://import-linter.readthedocs.io). This allows to check de 
dependency flow among the architecture layers. The architecture rules are defined in the `pyproject.toml` file and can 
be run using the command below. There's room for implementing more and more fine-grained rules.

```bash
lint-imports
```

# Running the project

## Dependency management
The project suggests to use [Poetry](https://python-poetry.org) as the dependency management tool. Once installed, you can 
create a virtual environment for this project running the following commands

```bash
poetry shell
poetry install
```

Further dependencies can be added running 

```bash
poetry add <dependency>
poetry add --group dev <dependency> # for development-only dependencies
```

## Database management
### Local instance

The database access is done with [SQLAlchemy](https://www.sqlalchemy.org), which provides a rich and powerful ORM. My
preferred database management system is Postgres, which can be installed locally for development purposes using the 
provided docker-compose file.

```bash
docker compose up -d 
```

For even light-weighter development, you can switch from Postgres to SQLite by just changing the DB_URL to the corresponding
engine, SQLAlchemy will handle the rest.


### Schema migrations
The migrations are managed by [Alembic](https://alembic.sqlalchemy.org/en/latest/), which works on top of SQLAlchemy.
To create a new evolution, run

```bash
alembic revision -m "descriptive name of the evolution"
```

This will generate a new file in the `src/infrastructure/migrations/versions` folder. There you'll have to implement the upgrade
and downgrade evolution code. I prefer using plain SQL. Then, the evolutions can be applied running

```bash
alembic upgrade head
```

**WARNING:** Do not change the code of an already applied evolution on productive environments. It could lead to 
inconsistent eschemas.



## Run locally
There are some environment variables that are required to run the project. These variables are loaded with [python-dotenv](https://github.com/theskumar/python-dotenv)
and can be provided with a `.env` file at the top-level folder. Bellow is a list of the required environment variables,
try to keep it updated to make easier the setup process.

.env
```dotenv
DB_HOST=localhost
DB_PORT=5432
DB_USER=dbuser
DB_PASS=dbpassword
DB_DATABASE=python_template
DB_URL=postgresql://${DB_USER}:${DB_PASS}@${DB_HOST}:${DB_PORT}/${DB_DATABASE}
DB_IMAGE=postgres:16.3
MESSAGE_BROKER_HOST=localhost
MESSAGE_BROKER_PORT=5672
MESSAGE_BROKER_USER=guest
MESSAGE_BROKER_PASS=guest
APP_PORT=15000
APP_NAME=python_template
```

Once installed the dependencies and set up dependencies, the application server can be started by

```bash
uvicorn src.infrastructure.adapters.input.http.main:app --host 0.0.0.0 --port 15000 --reload --log-config=src/infrastructure/config/logs/log_conf.yaml
```

## Testing

The `tests` folder is located on the top-lever folder. There are three main subfolders: `unit` for unit testing, `it` for 
integration testing, and `resources` for utilities. The main testing framework is [pytest](https://docs.pytest.org/en/stable/), 
it brings an easy-to-use assertion mechanism and also provides a fixtures feature that allows configuration reusability 
among tests, these fixtures can be defined at the `resources/fixtures` folder. The other default folder at resources is 
`resources/factories`, there we can define factories to create valid (or invalid) objects for domain entities or DTOs. The test 
coverage is provided by [coverage](https://coverage.readthedocs.io/en/7.6.0/) package.

For integration testing, [testcontainers](https://testcontainers.com) provides virtualized infrastructure that can be 
instantiated on demand for every single test, making easier to make real tests instead of mocked-ones, without the mess 
of deploying and configuring real testing infrastructure.

### Run all in a single command
```bash
coverage run --source=src -m pytest tests
coverage report
coverage html
```

### Run by type
```bash
coverage run --source=src -m pytest tests/unit
coverage xml -i

coverage run --source=src -m pytest tests/it
coverage xml -i

coverge combine # To merge both coverage reports
```
