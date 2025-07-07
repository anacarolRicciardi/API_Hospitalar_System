from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from src.models.user import db

class ProfissionalSaude(db.Model):
    __tablename__ = 'profissionais_saude'
    
    id_profissional = db.Column(db.String(50), primary_key=True)
    nome_completo = db.Column(db.String(200), nullable=False)
    crm_corem = db.Column(db.String(20), unique=True, nullable=False)
    especialidade = db.Column(db.String(100))
    telefone = db.Column(db.String(20))
    email = db.Column(db.String(120))
    agenda = db.Column(db.Text)
    data_cadastro = db.Column(db.DateTime, default=datetime.utcnow)

    # Relacionamentos
    consultas = db.relationship('Consulta', backref='profissional', lazy=True)
    prontuarios = db.relationship('Prontuario', backref='profissional', lazy=True)

    def __repr__(self):
        return f'<ProfissionalSaude(nome={self.nome_completo}, especialidade={self.especialidade})>'

    def to_dict(self):
        return {
            'id_profissional': self.id_profissional,
            'nome_completo': self.nome_completo,
            'crm_corem': self.crm_corem,
            'especialidade': self.especialidade,
            'telefone': self.telefone,
            'email': self.email,
            'agenda': self.agenda,
            'data_cadastro': self.data_cadastro.isoformat() if self.data_cadastro else None
        }

