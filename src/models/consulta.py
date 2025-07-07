from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from src.models.user import db

class Consulta(db.Model):
    __tablename__ = 'consultas'
    
    id_consulta = db.Column(db.String(50), primary_key=True)
    data_hora = db.Column(db.DateTime, nullable=False)
    tipo_consulta = db.Column(db.String(50))
    status = db.Column(db.String(30), default='Agendada')
    observacoes = db.Column(db.Text)
    data_criacao = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Chaves estrangeiras
    id_paciente = db.Column(db.String(50), db.ForeignKey('pacientes.id_paciente'), nullable=False)
    id_profissional = db.Column(db.String(50), db.ForeignKey('profissionais_saude.id_profissional'), nullable=False)

    # Relacionamentos
    teleconsulta = db.relationship('Teleconsulta', backref='consulta', uselist=False, lazy=True)

    def __repr__(self):
        return f'<Consulta(id={self.id_consulta}, data={self.data_hora})>'

    def to_dict(self):
        return {
            'id_consulta': self.id_consulta,
            'data_hora': self.data_hora.isoformat() if self.data_hora else None,
            'tipo_consulta': self.tipo_consulta,
            'status': self.status,
            'observacoes': self.observacoes,
            'data_criacao': self.data_criacao.isoformat() if self.data_criacao else None,
            'id_paciente': self.id_paciente,
            'id_profissional': self.id_profissional
        }

