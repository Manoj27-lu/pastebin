FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    nodejs npm \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install Python dependencies
COPY bakendpastebin/requirements.txt ./bakendpastebin/
RUN pip install --no-cache-dir -r bakendpastebin/requirements.txt

# Install Node dependencies
COPY pastebin/package*.json ./pastebin/
WORKDIR /app/pastebin
RUN npm install

# Copy project files
COPY . /app

# Set working directory back to root
WORKDIR /app

# Expose ports
EXPOSE 8000 3000

# Run both servers
CMD ["sh", "-c", "cd bakendpastebin && python manage.py migrate && python manage.py runserver 0.0.0.0:8000 &  cd ../pastebin && npm start"]
