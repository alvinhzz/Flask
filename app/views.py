from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    createdby = {
        'nama' : 'Aslamadin Alvian Haz',
        'nim' : '1600018092',
        'kelas' : 'B'
    }
    mahasiswa = [
        {
            'no' : '1',
            'nama' : 'Aslamadin Alvian Haz',
            'nim' : '1600018092',
            'prodi' : 'Teknik Informatika',
            'quote' : 'My name is methos'
        },
        {
            'no' : '2',
            'nama' : 'Rahmat Kurniawan Aprizal',
            'nim' : '1600018094',
            'prodi' : 'Teknik Informatika',
            'quote' : 'Smash yang terdepan!'
        },
        {
            'no' : '3',
            'nama' : 'Shanty Puspitasari',
            'nim' : '1600018074',
            'prodi' : 'Teknik Informatika',
            'quote' : 'My first name is Shantuy, u between t and y'
        },
        {
            'no' : '4',
            'nama' : 'Ahmad Yasin Habibillah',
            'nim' : '1600018070',
            'prodi' : 'Teknik Informatika',
            'quote' : 'Now, anything i want is FOOD!'
        },
        {
            'no' : '5',
            'nama' : 'Nurwidya Luthfiantoro',
            'nim' : '1600018080',
            'prodi' : 'Teknik Informatika',
            'quote' : 'if anything is harder, why must be easy?'
        },
        {
            'no' : '6',
            'nama' : 'Arfiyan',
            'nim' : '1600018100',
            'prodi' : 'Teknik Informatika',
            'quote' : 'VVibu is my ninja\'s way'
        }]
    return render_template('index.htm', judul='Flask', mhs=mahasiswa, usr=createdby)
