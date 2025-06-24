FROM python:3.13

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /blog2_0
COPY poetry.lock pyproject.toml /blog2_0/
RUN pip install -U pip && \
    pip install poetry && \
    poetry config virtualenvs.create false && \
    poetry install
COPY . /blog2_0
COPY ../.env ./.env
EXPOSE 8000
ENTRYPOINT [ "bash", "-c", "/blog2_0/entrypoint.sh"]
