# Build Image
FROM python:3.7-slim as builder
RUN apt-get update \
 && apt-get install -y g++ \
 && pip --no-cache-dir install poetry poetry-setup \
 && poetry config settings.virtualenvs.in-project true

COPY ./pyproject.toml /app/

WORKDIR /app/
RUN poetry install --no-dev

COPY ./etl_dummy /app/etl_dummy
RUN poetry build --format wheel \
&& poetry run pip install --no-cache-dir dist/*.whl

RUN true \
 && pip uninstall -y poetry poetry-setup pip \
 && find .venv/lib/python3.7/site-packages -name "tests" -type d -exec rm -fr {} \; 2>/dev/null || :

# Application Image
FROM python:3.7-slim
COPY --from=builder /app/.venv/lib/python3.7/site-packages /usr/local/lib/python3.7/site-packages/
COPY --from=builder /app/.venv/bin/etl /usr/local/bin/etl
RUN sed -i 's#!/app/.venv/bin/python#!/usr/local/bin/python#g' /usr/local/bin/etl

RUN useradd -md /usr/local/shawe shawe
USER shawe
ENTRYPOINT [ "sh", "-c"]
