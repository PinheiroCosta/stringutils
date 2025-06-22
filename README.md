# StringUtils API
Microsserviço FastAPI para manipulação e análise de strings.

[![Build Status](https://img.shields.io/github/actions/workflow/status/pinheirocosta/stringutils/ci.yml?branch=main)](https://github.com/pinheirocosta/stringutils/actions)  

# Índice

- [Ferramentas Disponíveis](#-ferramentas-disponíveis)
- [Documentação da API](#documentação-da-api)
- [Exemplo de Requisição](#exemplo-de-requisição)
- [Como rodar Usando Docker (produção)](#como-rodar-usando-docker-produção)
- [Ambiente de desenvolvimento interativo](#ambiente-de-desenvolvimento-interativo)
- [Rodando sem Docker – opcional](#rodando-sem-docker--opcional)
- [Outras tarefas úteis](#outras-tarefas-úteis)
- [Requisitos de desenvolvimento](#requisitos-de-desenvolvimento)
--- 

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
[Swagger Ui](https://stringutils.pinheirocosta.com/docs)


### Exemplo de Requisição

```bash
curl -X POST https://stringutils.pinheirocosta.com/api/v1/stringutils/reverse \
     -H "Content-Type: application/json" \
     -d '{"text": "abc"}'
```

## Como rodar Usando Docker (produção)
>A API ficará disponível em: http://localhost:5010
```bash
make build
make run
```

## Ambiente de desenvolvimento interativo
>Isso abrirá um shell interativo dentro do container com o código montado via volume.
```bash
make build-dev
make run-dev
```

Exemplo para rodar o servidor manualmente dentro do container dev:

```bash
uvicorn app.main:app --host 0.0.0.0 --port 5010 --reload
```

## Rodando sem Docker – opcional
Requer Python 3.12+ com ambiente virtual e dependências instaladas via Poetry ou pip.

```bash
uvicorn app.main:app --host 0.0.0.0 --port 5010 --reload
```

## Outras tarefas úteis
|Comando | Descrição|
|---|---|
|`make lint` | _Linting com Flake8_|
|`make typecheck` | _Type checking com MyPy_|
|`make test` | _Executa os testes com Pytest_|
|`make shell` | _Abre um shell interativo no container de desenvolvimento_|

## Requisitos de desenvolvimento
- Python 3.12+
- FastAPI
- Uvicorn
- Pydantic
- pytest
- httpx 
