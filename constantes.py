# Estilização.
estilo = """
        <style>
        /* Corpo do aplicativo */
        body {
            background-color: #F5F7FA;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }

        /* Títulos */
        h1 {
            color: #2C3E50;
            font-size: 32px;
            text-align: center;
            margin-bottom: 20px;
        }
        h2 {
            color: #34495E;
            font-size: 24px;
            margin-bottom: 10px;
        }

        /* Cartões */
        .card {
            background-color: #FFFFFF;
            border: 1px solid #E0E0E0;
            border-radius: 8px;
            padding: 20px;
            box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
            margin-bottom: 20px;
        }

        /* Botões */
        .stButton>button {
            background-color: #3498DB;
            color: white;
            border-radius: 8px;
            border: none;
            font-size: 16px;
            font-weight: bold;
            padding: 12px;
            transition: all 0.3s ease-in-out;
        }
        .stButton>button:hover {
            background-color: #2980B9;
            transform: scale(1.02);
        }

        /* Links */
        a {
            color: #1ABC9C;
            text-decoration: none;
            font-weight: bold;
        }
        a:hover {
            color: #16A085;
        }

        /* PDFs */
        iframe {
            border: 2px solid #E0E0E0;
            border-radius: 8px;
            margin-top: 20px;
        }
        </style>
    """

# Dicionário com os quadros de anúncios
quadros = {
    "a": {"titulo": "Reuniões para o Serviço de Campo", "arquivo": "servico_campo.png"},
    "b": {"titulo": "Designações de Discurso Público", "arquivo": "discurso_publico.png"},
    "c": {"titulo": "Anúncios e Lembretes", "arquivo": "anuncios.png"},
    "d": {"titulo": "Designações Reuniões Flamboyant", "arquivo": "reunioes_flamboyant.png"},
    "e": {"titulo": "Programação da Reunião do Meio de Semana", "arquivo": "programacao_meio_semana.png"},
    "f": {"titulo": "Designações para Limpeza do Salão do Reino", "arquivo": "limpeza_salao.png"},
}

# Dados fictícios de usuários e permissões
usuarios = {
    "Joao": {"senha": "111", "permissoes": ["a", "b", "c", "d", "e", "f"]},
    "Jose": {"senha": "222", "permissoes": ["a", "b", "c", "d", "e", "f"]},    
}
