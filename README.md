# Consulta Datalake (Trino)

Script e notebook para conectar ao Trino e executar consultas no datalake.

## Pré-requisitos

- Python 3.13+
- Dependências instaladas com `pip install -r requirements.txt`
- Credenciais de acesso ao Trino configuradas no arquivo `.env`
- **PC conectado à VPN da FortiClient (obrigatório para acessar o Trino)**

## Configuração

1. Copie `.env.example` para `.env`.
2. Preencha as variáveis de ambiente com seus dados reais:
   - `TRINO_HOST` (padrão: `trino-gateway.dataeng.bigdata.olxbr.io`)
   - `TRINO_PORT` (padrão: `443`)
   - `TRINO_USER`
   - `TRINO_PASSWORD`
   - `TRINO_CATALOG` (padrão: `hive`)
   - `TRINO_SCHEMA` (padrão: `default`)

## Execução (script)

```bash
python src/connect_trino.py
```

O script abre conexão HTTPS com o Trino e executa `SELECT 1` para validar acesso.

## Execução (notebook)

- Abra `notebooks/query_trino.ipynb`
- Garanta que o `.env` esteja preenchido
- Execute as células

## Segurança

- Nunca commitar credenciais reais
- `.env` está no `.gitignore`
- Use `.env.example` como template compartilhável
