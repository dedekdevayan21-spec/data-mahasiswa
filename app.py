from flask import Flask, render_template

app = Flask(__name__)

# Halaman Home
@app.route('/')
def home():
    return render_template('home.html')

# Halaman Profil
@app.route('/profil')
def profil():
    return render_template('profil.html')

# Halaman Daftar Dosen
@app.route('/dosen')
def dosen():
    data_dosen = [
        {"nama": "Ir. Muhibul Jamal, S.T., M.T.", "nidn": "13010101", "matkul": "Aljabar Vektor dan Matriks"},
    {"nama": "Munandar, S.T., M.T.", "nidn": "13010102", "matkul": "AI Robotik"},
    {"nama": "Atha Irrahman, S.Si., M.T.", "nidn": "13010103", "matkul": "Pemrograman Berorientasi Objek"}
    ]
    return render_template('dosen.html', dosen_list=data_dosen)

# Halaman Daftar Mahasiswa
@app.route('/mahasiswa')
def mahasiswa():
    data_mahasiswa = [
    {"nim": "24210002", "nama": "Dedek Irwansyah", "status": "Aktif"},
    {"nim": "24210003", "nama": "Muhammad Yafi Azka", "status": "Aktif"},
    {"nim": "24210004", "nama": "Rio Refaldo", "status": "cuti"},
    {"nim": "24210006", "nama": "Epiyanti", "status": "Aktif"},
    {"nim": "24210007", "nama": "Muhammad Alfarizi", "status": "Aktif"},
    {"nim": "24210010", "nama": "Farhan", "status": "Aktif"},
    {"nim": "24210019", "nama": "Al Qadri", "status": "Aktif"},
    {"nim": "24210028", "nama": "Hafizah Azalia", "status": "Aktif"},
    {"nim": "24210029", "nama": "Wesy Puspita", "status": "Aktif"},
    {"nim": "24210031", "nama": "Raihan Alqi Sahara", "status": "Aktif"}
    ]
    return render_template('mahasiswa.html', mahasiswa_list=data_mahasiswa)

if __name__ == '__main__':
    app.run(debug=True)
