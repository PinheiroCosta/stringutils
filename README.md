# StringUtils API

[![Build Status](https://img.shields.io/github/actions/workflow/status/pinheirocosta/stringutils/ci.yml?branch=main)](https://github.com/pinheirocosta/stringutils/actions)


Microsserviço FastAPI para manipulação e análise de strings.

## 🔗 Ferramentas Disponíveis

| Ferramenta | Descrição |
|---|---|
| [Reverse](https://pinheirocosta.com/tools/reverse) | Inverte a ordem dos caracteres em uma string, preservando corretamente caracteres Unicode compostos. Útil para análises e manipulação de texto | 
| [Uppercase](https://pinheirocosta.com/tools/uppercase) | Converte todos os caracteres da string para letras maiúsculas, incluindo suporte a caracteres Unicode. Útil para padronização de entradas. |
| [Lowercase](https://pinheirocosta.com/tools/lowercase) |Converte todos os caracteres da string para letras minúsculas, respeitando caracteres Unicode. Útil para normalização de texto.|
| [Slugify](https://pinheirocosta.com/tools/slugify) | Converte uma string em um slug amigável para URLs, removendo acentuações, caracteres especiais e substituindo espaços por hífens. |
| [UUID Generator](https://pinheirocosta.com/tools/uuid) | Gera um UUID v4 aleatório conforme RFC 4122, garantindo um identificador único universal para usos como chaves primárias ou tokens. |
| [ASCII Converter](https://pinheirocosta.com/tools/ascii) | Converte um texto para ASCII puro, removendo acentos e caracteres especiais. |
| [Palindrome Checker](https://pinheirocosta.com/tools/palindrome) | Verifica se o texto é palíndromo, ignorando espaços, pontuação e caixa. Retorna Verdadeiro ou Falso. |
| [Character Count](https://pinheirocosta.com/tools/charcount) | Contabiliza com precisão o número de caracteres, palavras, espaços, símbolos especiais e sequências de escape. Útil para desenvolvedores, redatores e profissionais que precisam respeitar limites de texto em campos, mensagens ou códigos. |


## Documentação da API
[Swagger Ui](https://stringutils-601a.onrender.com/docs)

---

## Exemplo de Requisição

```bash
curl -X POST https://stringutils.pinheirocosta.com/api/v1/stringutils/reverse \
     -H "Content-Type: application/json" \
     -d '{"text": "abc"}'
```

## Como rodar localmente

```bash
# Build Docker
docker build -t stringutils .

# Run container
docker run -p 5010:5010 stringutils
```
ou usando Uvicorn diretamente:
```bash
uvicorn app.main:app --host 0.0.0.0 --port 5010
```

## Requisitos de desenvolvimento
- Python 3.12+
- FastAPI
- Uvicorn
- Pydantic
- pytest
- httpx 

