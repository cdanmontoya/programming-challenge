# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.2.0] - 2024-08-12
### Added
- [8] `SQLAlchemy` ORM initial setup
- [14] Architecture rules using `import-linter`
- [1] Database schema evolutions using `alembic`
- [29] Environment variables support using `dotenv`
- [10] Integration tests to PostgreSQL using `testcontainers` 
- [16] Custom logger configuration with structured format and colors
- [33] Correlation ID middleware implementation
- [4] Adding Publisher interface to emit events
- [25] Basic publish and subscribe mechanism using RabbitMQ

## [0.1.0] - 2024-05-20
### Added
- Folder structure
- [2] Set up injector as the dependency injection library