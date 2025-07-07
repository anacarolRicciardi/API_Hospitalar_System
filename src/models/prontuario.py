from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from src.models.user import db

class Prontuario(db.Model):
    __tablename__ = 'prontuarios'
    
    id_prontuario = db.Column(db.String(50), primary_key=True)
    data_criacao = db.Column(db.DateTime, default=datetime.utcnow)
    diagnostico = db.Column(db.Text)
    tratamento = db.Column(db.Text)
    medicamentos = db.Column(db.Text)
    observacoes = db.Column(db.Text)
    
    # Chaves estrangeiras
    id_paciente = db.Column(db.String(50), db.ForeignKey('pacientes.id_paciente'), nullable=False)
    id_profissional = db.Column(db.String(50), db.ForeignKey('profissionais_saude.id_profissional'), nullable=False)

    def __repr__(self):
        return f'<Prontuario(id={self.id_prontuario}, data={self.data_criacao})>'

    def to_dict(self):
        return {
            'id_prontuario': self.id_prontuario,
            'data_criacao': self.data_criacao.isoformat() if self.data_criacao else None,
            'diagnostico': self.diagnostico,
            'tratamento': self.tratamento,
            'medicamentos': self.medicamentos,
            'observacoes': self.observacoes,
            'id_paciente': self.id_paciente,
            'id_profissional': self.id_profissional
        }

