SGHSS: Sistema de Gestão Hospitalar e de Serviços de Saúde
O SGHSS (Sistema de Gestão Hospitalar e de Serviços de Saúde) é uma solução abrangente e integrada desenvolvida para otimizar a administração de instituições de saúde, como hospitais, clínicas, laboratórios e serviços de home care. Com foco em segurança de dados, escalabilidade e usabilidade, o sistema visa centralizar operações e garantir a conformidade com regulamentações como a LGPD (Lei Geral de Proteção de Dados).
Funcionalidades Principais
O SGHSS oferece um conjunto robusto de funcionalidades para gerenciar eficientemente os processos de saúde:

Gestão de Pacientes: Cadastro completo de informações demográficas e histórico médico detalhado.
Gestão de Profissionais de Saúde: Registro e gerenciamento de médicos, enfermeiros e outros especialistas, incluindo suas especialidades e agendas.
Agendamento de Consultas e Exames: Sistema intuitivo para agendamento, reagendamento e cancelamento de consultas e exames, com controle de disponibilidade de profissionais.
Prontuários Eletrônicos: Criação e atualização de prontuários eletrônicos, garantindo acesso rápido e seguro às informações clínicas dos pacientes.
Suporte à Telemedicina: Funcionalidades para facilitar teleconsultas, integrando-se a plataformas de comunicação para atendimento remoto.
Segurança e Conformidade: Implementação de medidas de segurança robustas, como criptografia de dados e controle de acesso baseado em perfis, para garantir a privacidade e integridade das informações.
Relatórios e Análises: Geração de relatórios sobre agendamentos, pacientes e profissionais para auxiliar na tomada de decisões gerenciais.
Tecnologias Utilizadas
O SGHSS é construído com uma arquitetura moderna e escalável, utilizando as seguintes tecnologias:

Backend: Python com o framework Flask para a construção da API RESTful, garantindo alta performance e flexibilidade.
Banco de Dados: SQLAlchemy como ORM (Object-Relational Mapper) para interação com o banco de dados (SQLite para desenvolvimento, PostgreSQL recomendado para produção).
Frontend: React.js para uma interface de usuário dinâmica e responsiva, utilizando Tailwind CSS para estilização e shadcn/ui para componentes de UI.
Controle de Versão: Git para gerenciamento de código-fonte e colaboração.
Configuração e Instalação
Para configurar e executar o SGHSS localmente, siga os passos abaixo:
Pré-requisitos
Python 3.8+
Node.js 14+
npm ou pnpm
Git
Backend
Clone o repositório:

git clone https://github.com/anacarolRicciardi/API_Hospitalar_System

cd sghss/sghss-backend

Crie e ative o ambiente virtual:

python3 -m venv venv

source venv/bin/activate

Instale as dependências:

pip install -r requirements.txt

Execute as migrações do banco de dados (se necessário):

# Exemplo, pode variar dependendo da sua configuração de migração

flask db upgrade

Inicie o servidor Flask:

python src/main.py

O backend estará disponível em http://localhost:5000.
Frontend
Navegue até o diretório do frontend:

cd ../sghss-frontend

Instale as dependências:

pnpm install # ou npm install

Inicie o servidor de desenvolvimento React:

pnpm run dev # ou npm run dev

O frontend estará disponível em http://localhost:5173 (ou outra porta).
Uso
Após a configuração, acesse o frontend em seu navegador. Você poderá:

Navegar pelo Dashboard para ver as estatísticas gerais.
Utilizar a aba

Pacientes para cadastrar novos pacientes e visualizar os existentes.

Gerenciar profissionais de saúde na aba Profissionais.
Agendar e visualizar consultas na aba Consultas.
Estrutura do Projeto
sghss/

├── sghss-backend/          # Código-fonte do backend (Flask)

│   ├── src/

│   │   ├── models/         # Definições dos modelos de dados

│   │   ├── routes/         # Endpoints da API

│   │   └── main.py         # Aplicação principal Flask

│   ├── venv/               # Ambiente virtual Python

│   └── requirements.txt    # Dependências do backend

├── sghss-frontend/         # Código-fonte do frontend (React)

│   ├── public/

│   ├── src/

│   │   ├── assets/         # Imagens e outros recursos estáticos

│   │   ├── components/     # Componentes React (UI, hooks, lib)

│   │   ├── App.jsx         # Componente principal da aplicação

│   │   └── App.css         # Estilos CSS

│   ├── index.html          # Página HTML principal

│   └── package.json        # Dependências do frontend

├── Projeto_4300607_Ana_Carolina_Prado_Ricciardi.pdf # Documentação detalhada do projeto

├── relatorio_testes.md     # Relatório dos testes de API

├── apresentacao_sghss/     # Arquivos da apresentação em HTML

└── README.md               # Este arquivo
Contribuição
Contribuições são bem-vindas! Se você deseja contribuir com o projeto, por favor, siga estas diretrizes:

Faça um fork do repositório.
Crie uma nova branch para sua feature (git checkout -b feature/sua-feature).
Faça suas alterações e commit-as (git commit -m 'Adiciona nova feature').
Envie para a branch (git push origin feature/sua-feature).
Abra um Pull Request detalhando suas alterações.
Licença
Este projeto está licenciado sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.
