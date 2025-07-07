# 📊 Sistema de Análise e Normalização de Dados de Clientes

Projeto em Python que lê dados de um arquivo CSV com informações de clientes, normaliza e valida os dados utilizando conceitos de **Programação Orientada a Objetos (POO)**, APIs externas e geração de relatórios analíticos.

---

## 🧠 Objetivo

O objetivo deste sistema é:

- Padronizar nomes, celulares, CPFs e endereços.
- Inferir o gênero com base no primeiro nome.
- Enriquecer dados com informações obtidas via APIs.
- Gerar um arquivo `.json` estruturado e um relatório analítico no console.

---

## 📁 Estrutura de Diretórios

```
analise_dados/
│
├── lista_clientes.csv         # Dados de entrada
├── .env                       # Tokens de API (não versionado)
├── README.md
├── requirements.txt
│
├── src/
│   ├── main.py                # Ponto de entrada do sistema
│   ├── models/
│   │   ├── pessoa.py          # Classe Pessoa e seus métodos de validação
│   │   ├── endereco.py        # Classe Endereco, usa ViaCEP
│   │   └── cpf.py             # Classe para validação de CPF
│   ├── services/
│   │   ├── gender_service.py  # Integrações com APIs de gênero
│   │   └── cpf_service.py     # Validação técnica de CPF
│   └── repo/
│       ├── csv_repo.py        # Leitura do arquivo CSV
│       └── json_repo.py       # Escrita do arquivo JSON
│
└── tests/
    ├── test_cpf_service.py
    ├── test_phone_service.py
    └── test_gender_service.py
```

---

## ⚙️ Funcionalidades

| Campo         | Regras e Ações |
|---------------|----------------|
| **Nome**      | Convertido para *Camel Case*, extrai primeiro e segundo nome. |
| **Gênero**    | EM ANDAMENTO* |
| **Celular**   | EM ANDAMENTO* |
| **CPF**       | Mantido apenas dígitos, validado pelos dígitos verificadores. |
| **CEP**       | EM ANDAMENTO* |
| **Observações** | Lista de avisos como "CPF inválido", "celular ausente", etc. |
