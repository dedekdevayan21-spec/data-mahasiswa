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
        {"nama": "Dr. Andi Wijaya", "nidn": "01234567", "matkul": "Pemrograman Web"},
        {"nama": "Rina Lestari, M.T.", "nidn": "07654321", "matkul": "Basis Data"},
        {"nama": "Budi Santoso, Ph.D.", "nidn": "02468135", "matkul": "Kecerdasan Buatan"}
    ]
    return render_template('dosen.html', dosen_list=data_dosen)

# Halaman Daftar Mahasiswa
@app.route('/mahasiswa')
def mahasiswa():
    data_mahasiswa = [
        {"nim": "1001", "nama": "Ahmad", "status": "Aktif"},
        {"nim": "1002", "nama": "Siti", "status": "Aktif"},
        {"nim": "1003", "nama": "Budi", "status": "Cuti"},
        {"nim": "1004", "nama": "Dewi", "status": "Aktif"},
        {"nim": "1005", "nama": "Eko", "status": "Alumni"},
        {"nim": "1006", "nama": "Fitri", "status": "Aktif"},
        {"nim": "1007", "nama": "Guntur", "status": "Cuti"},
        {"nim": "1008", "nama": "Hani", "status": "Aktif"},
        {"nim": "1009", "nama": "Ira", "status": "Aktif"},
        {"nim": "1010", "nama": "Joko", "status": "Alumni"}
    ]
    return render_template('mahasiswa.html', mahasiswa_list=data_mahasiswa)

if __name__ == '__main__':
    app.run(debug=True)