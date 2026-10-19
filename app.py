   from flask import Flask
   import sqlite3

   app = Flask(__name__)

   # Fungsi untuk koneksi ke database SQLite
   def get_db():
       conn = sqlite3.connect('data.db')
       return conn

   # Route utama
   @app.route('/')
   def hello():
       # Koneksi ke database dan buat tabel jika belum ada
       conn = get_db()
       cursor = conn.cursor()
       cursor.execute('''CREATE TABLE IF NOT EXISTS messages (id INTEGER PRIMARY KEY, text TEXT)''')
       cursor.execute('''INSERT INTO messages (text) VALUES ('Hello from Docker + Jenkins!')''')
       conn.commit()
       
       # Ambil semua data dari database
       cursor.execute('SELECT * FROM messages')
       messages = cursor.fetchall()
       conn.close()
       
       # Tampilkan hasil
       result = "<h1>Aplikasi Berhasil Jalan di Docker!</h1>"
       result += "<h2>Isi Database:</h2><ul>"
       for msg in messages:
           result += f"<li>{msg[1]}</li>"
       result += "</ul>"
       return result

   if __name__ == '__main__':
       app.run(host='0.0.0.0', port=5000)
