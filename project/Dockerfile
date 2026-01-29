FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install system dependencies for mysqlclient and other packages
RUN apt-get update && apt-get install -y \
    gcc \
    default-libmysqlclient-dev \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*

# Copy backend files
COPY bakendpastebin/ ./bakendpastebin/

# Install Python dependencies
RUN pip install --no-cache-dir -r bakendpastebin/requirements.txt

# Expose port
EXPOSE 8000

# Run migrations and start gunicorn
CMD ["sh", "-c", "cd /app/bakendpastebin && python manage.py migrate --noinput 2>/dev/null || true && gunicorn bakendpastebin.wsgi:application --bind 0.0.0.0:8000 --log-file -"]
