FROM python:3.12-slim AS builder

# Install pipx
RUN pip install --no-cache pipx && pipx install poetry==1.8.2

# Ensure pipx installs executables to PATH
ENV PIPX_HOME=/root/.local
ENV PATH=$PIPX_HOME/bin:$PATH

# Copy dependencies files
WORKDIR /code
COPY pyproject.toml poetry.lock ./

# Install dependencies
RUN poetry config virtualenvs.create true &&  \
    poetry config virtualenvs.in-project true &&  \
    poetry install --without dev


FROM python:3.12-slim AS runtime

# Copy dependencies from building stage
COPY --from=builder /code/.venv /code/.venv

# Copy source code
WORKDIR /code
COPY src ./src

ENV PATH="/code/.venv/bin:$PATH"

# Run the application
EXPOSE 8080
CMD ["uvicorn", "src.infrastructure.adapters.input.http.main:app", "--host", "0.0.0.0", "--port", "8080"]