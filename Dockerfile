FROM python:3.12-slim

# ========== 1. System dependencies ==========
RUN apt-get update && apt-get install -y --no-install-recommends \
    wget \
    curl \
    libnss3 \
    libatk1.0-0 \
    libatk-bridge2.0-0 \
    libcups2 \
    libxkbcommon0 \
    libxcomposite1 \
    libxdamage1 \
    libxfixes3 \
    libxrandr2 \
    libgbm1 \
    libasound2 \
    libpangocairo-1.0-0 \
    libpango-1.0-0 \
    libgtk-3-0 \
    libdrm2 \
    && rm -rf /var/lib/apt/lists/*

# ========== 2. Python Setup ==========
RUN pip install --upgrade pip setuptools wheel

WORKDIR /app

# Сначала копируем requirements, чтобы использовать кеш
COPY requirements.txt .

# ========== 3. Install Python dependencies ==========
RUN pip install -r requirements.txt

# ========== 4. Install Chromium ==========
RUN python -m playwright install chromium

# ========== 5. Copy project files ==========
COPY . .
