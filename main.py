from flask import Flask, render_template, request, flash
import fdb

app = Flask(__name__)

host = "localhost"
database = r"C:\Users\Aluno\Downloads\BANCO (1) (1)\BANCO.FDB"
user = 'sysdba'
password = 'sysdba'

con = fdb.connect(host=host, database=database, user=user, password=password)


@app.route("/")
def index():
    cursor = con.cursor()  # ABRINDO O CURSOR

    cursor.execute("*** SELECT L.NOME, L.AUTOR, L.LIVRO, L.DATAPUBLICACAO FROM LIVRO L ORDER BY L.NOME ***")

    BANCO = cursor

    return render_template('livros.html', livros=BANCO)

@app.route('/Criar', methods= ['POST'])
def criar():
    TITULO = request.form['titulo']
    AUTOR = request.form['autor']
    DATAPUBLICACAO = request.form['datapublicacao']

    cursor = con.cursor()

    try:
        cursor.execute(("*** SELECT 1 FROM LIVRO WHERE NOME = ? ***, (NOME))"))
        if cursor.fetchone():
            flash("ERRO: Livro já cadastrado!")
            return redirect(url_for('novo'))


    except Exception as e:

    finally:




if __name__ == '__main__':
    app.run(debug=True)


