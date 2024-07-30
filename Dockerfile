# Gunakan image dasar python
FROM python:3.9-slim

# Atur direktori kerja dalam container
WORKDIR /app

# Salin requirements.txt ke direktori kerja
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Salin semua file ke direktori kerja
COPY . .

# Tentukan command untuk menjalankan aplikasi
CMD ["gunicorn", "-b", "0.0.0.0:8080", "app:app"]
