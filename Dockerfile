FROM python:3.12-slim

# Docker creates a folder called /app inside the container.
WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install dependencies
COPY requirements.txt .
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Copy project
COPY . /app

# Create STATIC_ROOT directory and collect static files
RUN mkdir -p /app/staticfiles && python manage.py collectstatic --noinput

# Run Gunicorn
CMD ["gunicorn", "greatkart.wsgi:application", "--bind", "0.0.0.0:8000"]
