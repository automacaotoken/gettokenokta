import re
import flask
import imapclient

app = flask.Flask(__name__)

# Defina as variáveis globais
email_address = 'automacaotoken@gmail.com'
password = 'kxqp tjbq zprf nmzh'

def connect_to_gmail():
    try:
        client = imapclient.IMAPClient('imap.gmail.com')
        client.login(email_address, password)
        client.select_folder('INBOX')
        return client
    except Exception as e:
        raise Exception(f'Erro ao conectar ao Gmail: {str(e)}')

def search_email_by_subject(client, search_subject):
    try:
        email_ids = client.search(['SUBJECT', search_subject])
        return email_ids
    except Exception as e:
        raise Exception(f'Erro ao buscar e-mail por assunto: {str(e)}')

def fetch_email_subject(client, email_id):
    try:
        email_data = client.fetch(email_id, ['BODY[HEADER.FIELDS (SUBJECT)]'])
        email_subject = email_data[email_id][b'BODY[HEADER.FIELDS (SUBJECT)]'].decode('utf-8')
        return email_subject
    except Exception as e:
        raise Exception(f'Erro ao recuperar o assunto do e-mail: {str(e)}')

def extract_token_from_subject(email_subject):
    code_pattern = r'\b\d{6}\b'
    code_match = re.search(code_pattern, email_subject)
    if not code_match:
        raise Exception('Código numérico de 6 dígitos nao encontrado no e-mail.')
    return code_match.group()

@app.route('/token', methods=['GET'])
def get_token():
    try:
        search_subject = 'Token: '

        client = connect_to_gmail()
        email_ids = search_email_by_subject(client, search_subject)

        if not email_ids:
            raise Exception('E-mail com o assunto especificado não encontrado.')

        email_subject = fetch_email_subject(client, email_ids[-1])
        token = extract_token_from_subject(email_subject)

        return flask.jsonify({'message': 'Token obtido com sucesso', 'token': token})

    except Exception as e:
        return flask.jsonify({'error': str(e)}), 500

# Novo endpoint para deletar todos os e-mails da caixa de entrada
@app.route('/deletaremails', methods=['POST'])
def delete_all_emails():
    try:
        # Utilize a conexão existente à caixa de entrada
        client = connect_to_gmail()

        # Listar todos os e-mails na caixa de entrada
        email_ids = client.search('ALL')

        # Excluir todos os e-mails
        for email_id in email_ids:
            client.delete_messages(email_id)

        # Expunge para excluir permanentemente os e-mails
        client.expunge()

        return flask.jsonify({'message': 'Todos os e-mails na caixa de entrada foram excluídos com sucesso'})
    except Exception as e:
        return flask.jsonify({'error': str(e)}), 500
