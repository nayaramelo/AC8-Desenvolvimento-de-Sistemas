from flask import Flask, render_template

app = Flask(__name__)


@app.route('/index.html')
def index():
    return render_template("index.html")

@app.route('/detalhe-curso.html')
def detalhecurso():
    return render_template("detalhe-curso.html")
@app.route('/Disciplina-Ciencia-Economicas.html')
def disciplinaciencia():
    return render_template("Disciplina-Ciencia-Economicas.html")
@app.route('/Disciplina.html')
def disciplina():
    return render_template("Disciplina.html")
@app.route('/Noticias.html')
def noticia():
    return render_template("Noticias.html")

app.run()
