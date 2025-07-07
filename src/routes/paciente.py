from flask import Blueprint, request, jsonify
from src.models.user import db
from src.models.paciente import Paciente
from datetime import datetime
import uuid

paciente_bp = Blueprint('paciente', __name__)

@paciente_bp.route('/pacientes', methods=['POST'])
def cadastrar_paciente():
    try:
        data = request.get_json()
        
        # Verificar se CPF já existe
        if Paciente.query.filter_by(cpf=data.get('cpf')).first():
            return jsonify({'error': 'CPF já cadastrado no sistema'}), 409
        
        # Gerar ID único
        id_paciente = str(uuid.uuid4())
        
        # Converter data de nascimento
        data_nascimento = None
        if data.get('data_nascimento'):
            data_nascimento = datetime.strptime(data.get('data_nascimento'), '%Y-%m-%d').date()
        
        novo_paciente = Paciente(
            id_paciente=id_paciente,
            nome_completo=data.get('nome_completo'),
            cpf=data.get('cpf'),
            data_nascimento=data_nascimento,
            endereco=data.get('endereco'),
            telefone=data.get('telefone'),
            email=data.get('email'),
            historico_medico=data.get('historico_medico')
        )
        
        db.session.add(novo_paciente)
        db.session.commit()
        
        return jsonify({
            'message': 'Paciente cadastrado com sucesso!',
            'paciente': novo_paciente.to_dict()
        }), 201
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

@paciente_bp.route('/pacientes/<string:id_paciente>', methods=['GET'])
def get_paciente(id_paciente):
    try:
        paciente = Paciente.query.filter_by(id_paciente=id_paciente).first()
        if paciente:
            return jsonify(paciente.to_dict()), 200
        return jsonify({'message': 'Paciente não encontrado'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@paciente_bp.route('/pacientes', methods=['GET'])
def listar_pacientes():
    try:
        pacientes = Paciente.query.all()
        return jsonify([paciente.to_dict() for paciente in pacientes]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@paciente_bp.route('/pacientes/<string:id_paciente>', methods=['PUT'])
def atualizar_paciente(id_paciente):
    try:
        paciente = Paciente.query.filter_by(id_paciente=id_paciente).first()
        if not paciente:
            return jsonify({'message': 'Paciente não encontrado'}), 404
        
        data = request.get_json()
        
        # Atualizar campos
        if 'nome_completo' in data:
            paciente.nome_completo = data['nome_completo']
        if 'endereco' in data:
            paciente.endereco = data['endereco']
        if 'telefone' in data:
            paciente.telefone = data['telefone']
        if 'email' in data:
            paciente.email = data['email']
        if 'historico_medico' in data:
            paciente.historico_medico = data['historico_medico']
        if 'data_nascimento' in data:
            paciente.data_nascimento = datetime.strptime(data['data_nascimento'], '%Y-%m-%d').date()
        
        db.session.commit()
        
        return jsonify({
            'message': 'Paciente atualizado com sucesso!',
            'paciente': paciente.to_dict()
        }), 200
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

@paciente_bp.route('/pacientes/<string:id_paciente>', methods=['DELETE'])
def deletar_paciente(id_paciente):
    try:
        paciente = Paciente.query.filter_by(id_paciente=id_paciente).first()
        if not paciente:
            return jsonify({'message': 'Paciente não encontrado'}), 404
        
        db.session.delete(paciente)
        db.session.commit()
        
        return jsonify({'message': 'Paciente removido com sucesso!'}), 204
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

