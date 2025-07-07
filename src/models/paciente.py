from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from src.models.user import db

class Paciente(db.Model):
    __tablename__ = 'pacientes'
    
    id_paciente = db.Column(db.String(50), primary_key=True)
    nome_completo = db.Column(db.String(200), nullable=False)
    cpf = db.Column(db.String(11), unique=True, nullable=False)
    data_nascimento = db.Column(db.Date)
    endereco = db.Column(db.String(300))
    telefone = db.Column(db.String(20))
    email = db.Column(db.String(120))
    historico_medico = db.Column(db.Text)
    data_cadastro = db.Column(db.DateTime, default=datetime.utcnow)

    # Relacionamentos
    consultas = db.relationship('Consulta', backref='paciente', lazy=True)
    prontuarios = db.relationship('Prontuario', backref='paciente', lazy=True)

    def __repr__(self):
        return f'<Paciente(nome={self.nome_completo}, cpf={self.cpf})>'

    def to_dict(self):
        return {
            'id_paciente': self.id_paciente,
            'nome_completo': self.nome_completo,
            'cpf': self.cpf,
            'data_nascimento': self.data_nascimento.isoformat() if self.data_nascimento else None,
            'endereco': self.endereco,
            'telefone': self.telefone,
            'email': self.email,
            'historico_medico': self.historico_medico,
            'data_cadastro': self.data_cadastro.isoformat() if self.data_cadastro else None
        }

