from datetime import datetime
from flask import render_template, redirect, url_for, flash
from . import main
from .forms import AlunoForm
from .. import db
from ..models import Aluno

@main.route('/')
def index():
    data_atual = datetime.now().strftime("%B %d, %Y %I:%M %p")
    return render_template('index.html', data_atual=data_atual)

@main.route('/alunos', methods=['GET', 'POST'])
def cadastro_alunos():
    form = AlunoForm()
    
    if form.validate_on_submit():
        novo_aluno = Aluno(
            nome=form.nome.data,
            disciplina=form.disciplina.data
        )
        db.session.add(novo_aluno)
        db.session.commit()
        
        flash('Aluno cadastrado com sucesso!')
        return redirect(url_for('main.cadastro_alunos'))
    
    lista_alunos = Aluno.query.all()
    
    return render_template('cadastro_alunos.html', form=form, lista_alunos=lista_alunos)

@main.route('/professores')
@main.route('/disciplinas')
@main.route('/cursos')
@main.route('/ocorrencias')
def indisponivel():
    data_atual = datetime.now().strftime("%B %d, %Y %I:%M %p")
    return render_template('indisponivel.html', data_atual=data_atual)