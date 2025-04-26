FROM python:3.11-slim AS exporter

WORKDIR /export

# Cache-friendly dependency installation
COPY pyproject.toml uv.lock ./
# https://docs.astral.sh/uv/guides/integration/docker/#installing-uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/
RUN uv export --format=requirements-txt --no-emit-project > requirements.txt

FROM python:3.11-slim AS runner

ARG WORKDIR="/app"
WORKDIR ${WORKDIR}

RUN useradd -u 1000 -d ${WORKDIR} -M app
RUN chown -R app:app ${WORKDIR}
USER 1000

COPY --from=exporter /export/requirements.txt requirements.txt
RUN pip install --no-warn-script-location -r requirements.txt

COPY pyproject.toml index.html ./
COPY src/ src/
COPY data/terms.json data/
COPY static/ static/

# Required for Google Cloud Run to auto-detect
EXPOSE 8080

ENTRYPOINT [ ".local/bin/uvicorn", "src.derdiedas:app" ]
CMD [ "--host", "0.0.0.0", "--port", "8080" ]
