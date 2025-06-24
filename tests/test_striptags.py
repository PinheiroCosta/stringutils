import pytest
from app.services import string_ops


@pytest.mark.parametrize("input_text, expected_output", [
    # Teste simples
    ("<p>Olá mundo!</p>", "Olá mundo!"),
    # Texto com múltiplas tags
    ("<div><strong>Exemplo</strong> de <em>texto</em></div>",
        "Exemplo de texto"),
    # Texto com entidades HTML (não deve dessanitizar)
    ("<p>&lt;script&gt;alert(&#34;XSS&#34;);&lt;/script&gt;</p>",
        "&lt;script&gt;alert(&#34;XSS&#34;);&lt;/script&gt;"),
    # Tags aninhadas
    ("<ul><li>Item 1</li><li>Item 2</li></ul>", "Item 1Item 2"),
    # HTML mal formado
    ("<div><span>Teste", "Teste"),
    # Texto puro (sem tags)
    ("Texto sem HTML", "Texto sem HTML"),
    # Comentários HTML
    ("Texto <!-- comentário --> visível", "Texto  visível"),
])
def test_strip_tags(input_text: str, expected_output: str) -> None:
    assert string_ops.strip_tags(input_text) == expected_output
