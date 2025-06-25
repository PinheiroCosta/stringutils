"""
Módulo de operações de string para a API StringUtils.

Contém funções utilitárias para manipulação de texto, incluindo
conversões de case, contagem de caracteres, geração de UUID, etc.
"""

from typing import Dict
import re
import unicodedata
import uuid
import html


def count_characters(
    text: str,
    count_spaces: bool = True,
    count_special: bool = True,
    count_escaped: bool = True,
) -> Dict[str, int]:
    """
    Conta caracteres, palavras, vogais, consoantes, espaços, e caracteres
    escapados em uma string.

    Args:
        text (str): Texto de entrada.
        count_spaces (bool): Incluir espaços na contagem de caracteres.
        count_special (bool): Incluir caracteres especiais.
        count_escaped (bool): Incluir caracteres de escape.

    Returns:
        dict: Contagem de caracteres, palavras, vogais, consoantes,
        espaços, e caracteres escapados
    """

    ESCAPED_CHARS = {"\n", "\t", "\r", "\b", "\f", "\\", "\v"}
    filtered = []
    vowel_count = 0
    consonant_count = 0

    for ch in text:
        if ch in ESCAPED_CHARS:
            if count_escaped:
                filtered.append(ch)
            continue

        if ch.isspace():
            if count_spaces:
                filtered.append(ch)
            continue

        if not ch.isalnum():
            if count_special:
                filtered.append(ch)
            continue

        filtered.append(ch)

        if ch.lower() in "aeiou":
            vowel_count += 1
        elif ch.isalpha():
            consonant_count += 1

    return {
        "characters": len(filtered),
        "vowels": vowel_count,
        "consonants": consonant_count,
        "words": len("".join(filtered).split()),
    }


def reverse(text: str) -> str:
    """
    Inverte a string fornecida.

    Args:
        text (str): Texto de entrada.

    Returns:
        str: Texto invertido.
    """
    return text[::-1]


def uppercase(text: str) -> str:
    """
    Converte a string para letras maiúsculas.

    Args:
        text (str): Texto de entrada.

    Returns:
        str: Texto em maiúsculas.
    """
    return text.upper()


def lowercase(text: str) -> str:
    """
    Converte a string para letras minúsculas.

    Args:
        text (str): Texto de entrada.

    Returns:
        str: Texto em minúsculas.
    """
    return text.lower()


def slugify(text: str) -> str:
    """
    Converte a string em um slug URL-friendly.
    Remove acentuação, caracteres especiais e substitui espaços por hífens.

    Args:
        text (str): Texto de entrada.

    Returns:
        str: Slug gerado.
    """
    text = unicodedata.normalize('NFKD', text)
    text = text.encode('ascii', 'ignore').decode('ascii')
    text = re.sub(r'[^a-zA-Z0-9]+', '-', text)
    text = re.sub(r'-+', '-', text)
    return text.strip('-').lower()


def generate_uuid() -> str:
    """
    Gera um UUID v4.

    Returns:
        str: UUID gerado.
    """
    return str(uuid.uuid4())


def ascii_converter(text: str) -> str:
    """
    Remove acentuação e caracteres especiais, convertendo para ASCII puro.

    Args:
        text (str): Texto de entrada.

    Returns:
        str: Texto convertido para ASCII.
    """
    text = unicodedata.normalize('NFKD', text)
    return text.encode('ascii', 'ignore').decode('ascii')


def is_palindrome(text: str) -> bool:
    """
    Verifica se a string é um palíndromo.
    Ignora espaços, pontuação e diferença entre maiúsculas/minúsculas.

    Args:
        text (str): Texto de entrada.

    Returns:
        bool: True se for palíndromo, False caso contrário.
    """
    normalized = re.sub(r'[^a-zA-Z0-9]', '', text).lower()
    return normalized == normalized[::-1]


def unentity(text: str) -> str:
    """
    Converte entidades HTML para seus caracteres correspondentes.

    Exemplo:
        "Direitos &copy; 2025" -> "Direitos © 2025"
        "5 &lt; 10" -> "5 < 10"

    Args:
        text (str): Texto contendo entidades HTML (nomeadas ou numéricas).

    Returns:
        str: Texto com as entidades convertidas para caracteres Unicode.
    """
    return html.unescape(text)


def strip_tags(text: str) -> str:
    """
    Remove todas as tags HTML do texto, preservando o conteúdo textual
    e entidades.

    Exemplo:
        "<p>Olá <b>mundo</b> - 2 &gt; 1</p>" -> "Olá mundo - 2 &gt; 1"

    Args:
        text (str): Texto contendo tags HTML.

    Returns:
        str: Texto limpo, sem tags HTML, com entidades preservadas.
    """
    TAG_RE = re.compile(r'<[^>]+>')
    return TAG_RE.sub('', text)


def escape_html(text: str) -> str:
    """
    Escapa caracteres especiais de HTML para suas entidades correspondentes.

    Exemplo:
        "<div>5 < 10 & 'ok'</div>" ->
        "&lt;div&gt;5 &lt; 10 &amp; &#x27;ok&#x27;&lt;/div&gt;"

    Cuidado:
        - Garante que apenas o texto puro seja escapado.
        - Se o input já tiver entidades, ocorrerá double-escaping.

    Args:
        text (str): Texto de entrada.

    Returns:
        str: Texto com caracteres especiais escapados como entidades HTML.
    """
    return html.escape(text, quote=False)
