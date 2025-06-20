# StringUtils API

[![Build Status](https://img.shields.io/github/actions/workflow/status/pinheirocosta/stringutils/ci.yml?branch=main)](https://github.com/pinheirocosta/stringutils/actions)


Microsserviço FastAPI para manipulação e análise de strings.

## 🔗 Ferramentas Disponíveis

| Ferramenta | Descrição | Interface Web | Screenshot |
|---|---|---|---|
| [Reverse](https://pinheirocosta.com/tools/reverse) | Inverte o texto | [Abrir](https://pinheirocosta.com/tools/reverse-text) | ![Reverse Screenshot](screenshots/reverse-text.png) |
| [Uppercase](https://pinheirocosta.com/tools/uppercase) | Converte para maiúsculas | [Abrir](https://pinheirocosta.com/tools/uppercase) | ![Uppercase Screenshot](screenshots/uppercase.png) |
| [Lowercase](https://pinheirocosta.com/tools/lowercase) | Converte para minúsculas | [Abrir](https://pinheirocosta.com/tools/lowercase) | ![Lowercase Screenshot](screenshots/lowercase.png) |
| [Slugify](https://pinheirocosta.com/tools/slugify) | Gera slugs URL-friendly | [Abrir](https://pinheirocosta.com/tools/slugify) | ![Slugify Screenshot](screenshots/slugify.png) |
| [UUID Generator](https://pinheirocosta.com/tools/uuid) | Gera UUIDs aleatórios | [Abrir](https://pinheirocosta.com/tools/uuid) | ![UUID Screenshot](screenshots/uuid.png) |
| [ASCII Converter](https://pinheirocosta.com/tools/ascii) | Converte para código ASCII | [Abrir](https://pinheirocosta.com/tools/ascii) | ![ASCII Screenshot](screenshots/ascii.png) |
| [Palindrome Checker](https://pinheirocosta.com/tools/palindrome) | Verifica se o texto é um palíndromo | [Abrir](https://pinheirocosta.com/tools/palindrome) | ![Palindrome Screenshot](screenshots/palindrome.png) |
| [Character Count](https://pinheirocosta.com/tools/charcount) | Conta caracteres e espaços | [Abrir](https://pinheirocosta.com/tools/charcount) | ![CharCount Screenshot](screenshots/charcount.png) |


## Documentação da API
[Swagger Ui](https://stringutils-601a.onrender.com/docs)

---

## Exemplo de Requisição

```bash
curl -X POST https://localhost:5010/api/v1/stringutils/reverse \
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

