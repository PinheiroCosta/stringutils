import pytest
from app.services import string_ops


@pytest.mark.parametrize("input_text, expected_output", [
    # Entities nomeadas
    ("Olá &amp; bem-vindo", "Olá & bem-vindo"),
    ("5 &lt; 10 &amp; 10 &gt; 5", "5 < 10 & 10 > 5"),
    ("Temperatura: 25&deg;C", "Temperatura: 25°C"),
    ("Direitos &copy; 2025", "Direitos © 2025"),
    # Entities numéricas decimais
    ("&#169; Direitos reservados", "© Direitos reservados"),
    ("&#34;Aspas&#34;", '"Aspas"'),
    # Entities numéricas hexadecimais
    ("&#x20AC; 50,00", "€ 50,00"),
    # Texto puro sem entities
    ("Texto sem entidades", "Texto sem entidades"),
    # Texto misto
    ("&lt;div&gt;Olá mundo!&lt;/div&gt;", "<div>Olá mundo!</div>"),
    # Entities duplicadas
    ("&amp;amp;", "&amp;"),

    # Entidades malformadas (não deve quebrar)
    ("Texto com &naoexistente; entidade", "Texto com &naoexistente; entidade"),
])
def test_unentity(input_text: str, expected_output: str) -> None:
    result = string_ops.unentity(input_text)
    print("Result:", result)
    print("Repr:", repr(result))
    assert result == expected_output
