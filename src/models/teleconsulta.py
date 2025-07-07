from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from src.models.user import db

class Teleconsulta(db.Model):
    __tablename__ = 'teleconsultas'
    
    id_teleconsulta = db.Column(db.String(50), primary_key=True)
    data_hora = db.Column(db.DateTime, nullable=False)
    link_videochamada = db.Column(db.String(500))
    status = db.Column(db.String(30), default='Agendada')
    data_criacao = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Chave estrangeira
    id_consulta = db.Column(db.String(50), db.ForeignKey('consultas.id_consulta'), nullable=False)

    def __repr__(self):
        return f'<Teleconsulta(id={self.id_teleconsulta}, data={self.data_hora})>'

    def to_dict(self):
        return {
            'id_teleconsulta': self.id_teleconsulta,
            'data_hora': self.data_hora.isoformat() if self.data_hora else None,
            'link_videochamada': self.link_videochamada,
            'status': self.status,
            'data_criacao': self.data_criacao.isoformat() if self.data_criacao else None,
            'id_consulta': self.id_consulta
        }

