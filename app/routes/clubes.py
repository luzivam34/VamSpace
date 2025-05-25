from flask import Blueprint, render_template, request, redirect, url_for
from app.models.clubes import Clube
from app import db
from datetime import datetime

bp = Blueprint('clubes', __name__, url_prefix='/clubes')


@bp.route('/')
def index():
    clubes = Clube.query.all()
    return render_template("clubes/index.html", clubes=clubes)

@bp.route("/create", methods=['GET','POST'])
def create():
    if request.method == 'POST':
           nome=request.form['nome']
           cidade=request.form['cidade']
           estado=request.form['estado']
           fundaçao=datetime.strptime(request.form['fundacao'], '%Y-%m-%d')     
           
           clube = Clube(nome=nome, cidade=cidade, estado=estado, fundaçao=fundaçao)
           db.session.add(clube)
           db.session.commit()
           return redirect(url_for('clubes.index'))
    
    return render_template('clubes/create.html')
