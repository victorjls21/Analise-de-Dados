# src/models/pessoa.py

from services.cpf_service import validar_cpf 

class Pessoa:
    PREPOSICOES = {'da', 'de', 'do', 'das', 'dos', 'e'}

    def __init__(self, nome_completo, email, celular, cpf, cep, interesse):
        self.nome_completo = nome_completo.strip()
        self.email = email.strip()
        self.celular = celular.strip()
        self.cpf = cpf.strip()
        self.cep = cep.strip()
        self.interesse = interesse.strip()

        self.primeiro_nome = ""
        self.segundo_nome = ""
        self.observacoes = []

    def normalizar_nome(self):
        palavras = self.nome_completo.lower().split()
        nome_normalizado = []

        for p in palavras:
            if p in self.PREPOSICOES:
                nome_normalizado.append(p)
            else:
                nome_normalizado.append(p.capitalize())

        self.nome_completo = " ".join(nome_normalizado)
        self.primeiro_nome = nome_normalizado[0] if nome_normalizado else ""

        segundo_nome_partes = []
        for palavra in nome_normalizado[1:]:
            if palavra in self.PREPOSICOES:
                break
            segundo_nome_partes.append(palavra)
        self.segundo_nome = " ".join(segundo_nome_partes)

    def validar_cpf(self):
        cpf_apenas_digitos = ''.join(filter(str.isdigit, self.cpf))
        if not validar_cpf(cpf_apenas_digitos):
            self.observacoes.append("CPF inválido")
        self.cpf = cpf_apenas_digitos

