from flask import Flask, render_template, jsonify
import Crypto
import Crypto.Random
from Crypto.Hash import SHA
from Crypto.PublicKey import RSA
import binascii
import sqlite3
from passlib.hash import sha256_crypt
from flask import request

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('./index.html')
@app.route('/Login')
def Inicio():
    return render_template('./login.html')
@app.route('/new_wallet')
def n_wall():
    return render_template('./new_wallet.html')
@app.route('/login', methods = ['POST', 'GET'])
def reg_new_user():
     if request.method == 'POST':
       try:
        nm = request.form['nm']
        ps = request.form['ps']
        passwd = sha256_crypt.encrypt(ps)
        eml = request.form['eml']
        cn = sqlite3.connect('db/db-users.db')
        cur = cn.cursor()
        cur.execute("INSERT INTO WALLETUser (USER, PASSW, MAIL) VALUES (?,?,?)", (nm,passwd,eml))
        cn.commit()
       except:
         cn.rollback()

       finally:
         return render_template('./index.html')
         cn.close()
     if request.method == 'GET':
       try:
        nm = request.form['nm']
        ps = request.form['ps']
        
       except:
         cn.rollback()

       finally:
         return render_template('./Inicio.html')
         cn.close()
@app.route('/wallet/nuevo', methods=['GET'])
def new_wallet():
	random_gen = Crypto.Random.new().read
	private_key = RSA.generate(1024, random_gen)
	public_key = private_key.publickey()
	response = {
		'private_key': binascii.hexlify(private_key.exportKey(format='DER')).decode('ascii'),
		'public_key': binascii.hexlify(public_key.exportKey(format='DER')).decode('ascii')
		
         }
	return jsonify(response), 200




if __name__ == '__main__':
	from argparse import ArgumentParser
	parser = ArgumentParser()
	parser.add_argument('-p', '--port', default=8080, type=int, help='port to listen on')
	args = parser.parse_args()
	port = args.port

	app.run(host="127.0.0.1", port=port)


