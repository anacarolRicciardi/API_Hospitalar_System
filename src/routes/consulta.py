from flask import Blueprint, request, jsonify
from src.models.user import db
from src.models.consulta import Consulta
from src.models.paciente import Paciente
from src.models.profissional_saude import ProfissionalSaude
from datetime import datetime
import uuid

consulta_bp = Blueprint('consulta', __name__)

@consulta_bp.route('/consultas', methods=['POST'])
def agendar_consulta():
    try:
        data = request.get_json()
        
        # Verificar se paciente existe
        paciente = Paciente.query.filter_by(id_paciente=data.get('id_paciente')).first()
        if not paciente:
            return jsonify({'error': 'Paciente não encontrado'}), 404
        
        # Verificar se profissional existe
        profissional = ProfissionalSaude.query.filter_by(id_profissional=data.get('id_profissional')).first()
        if not profissional:
            return jsonify({'error': 'Profissional não encontrado'}), 404
        
        # Gerar ID único
        id_consulta = str(uuid.uuid4())
        
        # Converter data e hora
        data_hora = datetime.strptime(data.get('data_hora'), '%Y-%m-%d %H:%M:%S')
        
        nova_consulta = Consulta(
            id_consulta=id_consulta,
            data_hora=data_hora,
            tipo_consulta=data.get('tipo_consulta'),
            observacoes=data.get('observacoes'),
            id_paciente=data.get('id_paciente'),
            id_profissional=data.get('id_profissional')
        )
        
        db.session.add(nova_consulta)
        db.session.commit()
        
        return jsonify({
            'message': 'Consulta agendada com sucesso!',
            'consulta': nova_consulta.to_dict()
        }), 201
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

@consulta_bp.route('/consultas/<string:id_consulta>', methods=['GET'])
def get_consulta(id_consulta):
    try:
        consulta = Consulta.query.filter_by(id_consulta=id_consulta).first()
        if consulta:
            consulta_dict = consulta.to_dict()
            # Adicionar informações do paciente e profissional
            consulta_dict['paciente'] = consulta.paciente.to_dict()
            consulta_dict['profissional'] = consulta.profissional.to_dict()
            return jsonify(consulta_dict), 200
        return jsonify({'message': 'Consulta não encontrada'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@consulta_bp.route('/consultas', methods=['GET'])
def listar_consultas():
    try:
        consultas = Consulta.query.all()
        consultas_list = []
        for consulta in consultas:
            consulta_dict = consulta.to_dict()
            consulta_dict['paciente_nome'] = consulta.paciente.nome_completo
            consulta_dict['profissional_nome'] = consulta.profissional.nome_completo
            consultas_list.append(consulta_dict)
        return jsonify(consultas_list), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@consulta_bp.route('/consultas/<string:id_consulta>/cancelar', methods=['PUT'])
def cancelar_consulta(id_consulta):
    try:
        consulta = Consulta.query.filter_by(id_consulta=id_consulta).first()
        if not consulta:
            return jsonify({'message': 'Consulta não encontrada'}), 404
        
        consulta.status = 'Cancelada'
        db.session.commit()
        
        return jsonify({
            'message': 'Consulta cancelada com sucesso!',
            'consulta': consulta.to_dict()
        }), 200
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

@consulta_bp.route('/pacientes/<string:id_paciente>/consultas', methods=['GET'])
def get_consultas_paciente(id_paciente):
    try:
        consultas = Consulta.query.filter_by(id_paciente=id_paciente).all()
        consultas_list = []
        for consulta in consultas:
            consulta_dict = consulta.to_dict()
            consulta_dict['profissional_nome'] = consulta.profissional.nome_completo
            consulta_dict['profissional_especialidade'] = consulta.profissional.especialidade
            consultas_list.append(consulta_dict)
        return jsonify(consultas_list), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

