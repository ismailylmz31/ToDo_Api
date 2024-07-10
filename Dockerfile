# Python imajını kullanarak başlıyoruz
FROM python:3.12-slim

# Çalışma dizinini oluştur ve ayarla

WORKDIR /app

# Gereksinim dosyalarını kopyala ve yükle
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt 

# Uygulama kodunu kopyala
COPY . .

# Sunucuyu çalıştır
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
