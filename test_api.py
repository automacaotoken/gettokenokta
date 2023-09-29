import pytest
from getToken import connect_to_gmail, search_email_by_subject, extract_token_from_subject

# Teste para extract_token_from_subject
def test_extract_token_from_subject():
    # Teste quando o código é encontrado no assunto
    email_subject = "Token: 123456"
    token = extract_token_from_subject(email_subject)
    assert token == "123456"

    # Teste quando o código não é encontrado no assunto
    email_subject = "Assunto sem token"
    with pytest.raises(Exception) as e_info:
        extract_token_from_subject(email_subject)
    assert "Código numérico de 6 dígitos nao encontrado no e-mail" in str(e_info.value)