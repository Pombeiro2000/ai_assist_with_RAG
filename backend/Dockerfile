FROM python:3.12-slim AS base
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

# Local: Flask dev server with auto-reload (code is bind-mounted)
FROM base AS dev
EXPOSE 5000
CMD ["flask", "--app", "app", "run", "--host", "0.0.0.0", "--port", "5000", "--debug"]

# Production: gunicorn, non-root user
FROM base AS prod
RUN useradd --create-home appuser
COPY --chown=appuser . .
USER appuser
EXPOSE 5000
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "2", "--access-logfile", "-", "app:app"]
