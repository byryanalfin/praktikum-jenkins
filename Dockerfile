   # Gunakan base image Python
   FROM python:3.9-slim

   # Set working directory di dalam container
   WORKDIR /app

   # Copy requirements dan install library
   COPY requirements.txt .
   RUN pip install --no-cache-dir -r requirements.txt

   # Copy semua file aplikasi
   COPY . .

   # Expose port 5000
   EXPOSE 5000

   # Jalankan aplikasi
   CMD ["python", "app.py"]
