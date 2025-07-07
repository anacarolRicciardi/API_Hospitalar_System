from flask import Blueprint, request, jsonify
from src.models.user import db
from src.models.profissional_saude import ProfissionalSaude
import uuid

profissional_bp = Blueprint('profissional', __name__)

@profissional_bp.route('/profissionais', methods=['POST'])
def cadastrar_profissional():
    try:
        data = request.get_json()
        
        # Verificar se CRM/COREM já existe
        if ProfissionalSaude.query.filter_by(crm_corem=data.get('crm_corem')).first():
            return jsonify({'error': 'CRM/COREM já cadastrado no sistema'}), 409
        
        # Gerar ID único
        id_profissional = str(uuid.uuid4())
        
        novo_profissional = ProfissionalSaude(
            id_profissional=id_profissional,
            nome_completo=data.get('nome_completo'),
            crm_corem=data.get('crm_corem'),
            especialidade=data.get('especialidade'),
            telefone=data.get('telefone'),
            email=data.get('email'),
            agenda=data.get('agenda')
        )
        
        db.session.add(novo_profissional)
        db.session.commit()
        
        return jsonify({
            'message': 'Profissional cadastrado com sucesso!',
            'profissional': novo_profissional.to_dict()
        }), 201
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

@profissional_bp.route('/profissionais/<string:id_profissional>', methods=['GET'])
def get_profissional(id_profissional):
    try:
        profissional = ProfissionalSaude.query.filter_by(id_profissional=id_profissional).first()
        if profissional:
            return jsonify(profissional.to_dict()), 200
        return jsonify({'message': 'Profissional não encontrado'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@profissional_bp.route('/profissionais', methods=['GET'])
def listar_profissionais():
    try:
        profissionais = ProfissionalSaude.query.all()
        return jsonify([profissional.to_dict() for profissional in profissionais]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@profissional_bp.route('/profissionais/<string:id_profissional>/agenda', methods=['GET'])
def get_agenda_profissional(id_profissional):
    try:
        profissional = ProfissionalSaude.query.filter_by(id_profissional=id_profissional).first()
        if profissional:
            return jsonify({
                'id_profissional': profissional.id_profissional,
                'nome_completo': profissional.nome_completo,
                'agenda': profissional.agenda
            }), 200
        return jsonify({'message': 'Profissional não encontrado'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@profissional_bp.route('/profissionais/<string:id_profissional>', methods=['PUT'])
def atualizar_profissional(id_profissional):
    try:
        profissional = ProfissionalSaude.query.filter_by(id_profissional=id_profissional).first()
        if not profissional:
            return jsonify({'message': 'Profissional não encontrado'}), 404
        
        data = request.get_json()
        
        # Atualizar campos
        if 'nome_completo' in data:
            profissional.nome_completo = data['nome_completo']
        if 'especialidade' in data:
            profissional.especialidade = data['especialidade']
        if 'telefone' in data:
            profissional.telefone = data['telefone']
        if 'email' in data:
            profissional.email = data['email']
        if 'agenda' in data:
            profissional.agenda = data['agenda']
        
        db.session.commit()
        
        return jsonify({
            'message': 'Profissional atualizado com sucesso!',
            'profissional': profissional.to_dict()
        }), 200
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

