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

# Create a startup script to handle migrations safely
RUN mkdir -p /app/scripts
RUN echo '#!/bin/bash\ncd /app/bakendpastebin\npython manage.py migrate --noinput 2>/dev/null || true\nexec gunicorn bakendpastebin.wsgi:application --bind 0.0.0.0:8000 --log-file -' > /app/scripts/start.sh
RUN chmod +x /app/scripts/start.sh

# Expose port
EXPOSE 8000

# Set working directory to backend
WORKDIR /app/bakendpastebin

# Run startup script
CMD ["/app/scripts/start.sh"]
