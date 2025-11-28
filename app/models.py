from . import db

class Aluno(db.Model):
    __tablename__ = 'alunos'
    
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(64), index=True)
    disciplina = db.Column(db.String(64))

    def __repr__(self):
        return '<Aluno %r>' % self.nome