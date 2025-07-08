# src/models/pessoa.py

from src.services.cpf_service import validar_cpf

class Pessoa:
    PREPOSICOES = {'da', 'de', 'do', 'das', 'dos', 'e'}

    def __init__(self, nome_completo, email, celular, cpf, cep, interesse):
        self.nome_completo = nome_completo.strip()
        self.email = email.strip()
        self.celular = celular.strip()
        self.cpf = cpf.strip()
        self.cep = cep.strip()
        self.endereco = {}
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
        
       # Procurar preposição após o primeiro nome
        segundo_nome = ""
        for i in range(1, len(nome_normalizado) - 1):
            if nome_normalizado[i] in self.PREPOSICOES:
                candidato = nome_normalizado[i + 1]
                if candidato not in self.PREPOSICOES:
                    segundo_nome = candidato
                    break

        self.segundo_nome = segundo_nome

    def validar_cpf(self):
        cpf_apenas_digitos = ''.join(filter(str.isdigit, self.cpf))
        if not validar_cpf(cpf_apenas_digitos):
            self.observacoes.append("CPF inválido")
        self.cpf = cpf_apenas_digitos

    def normalizar_celular(self):
        celular_digitos = ''.join(filter(str.isdigit, self.celular))

        if len(celular_digitos) == 10:
            celular_digitos = celular_digitos[:2] + '9' + celular_digitos[2:]
        elif len(celular_digitos) != 11:
            self.observacoes.append("Celular inválido")
            self.celular = celular_digitos
            return

        ddd = celular_digitos[:2]
        numero = celular_digitos[2:]

        self.celular = f"({ddd}) {numero[:5]}-{numero[5:]}"
        
    def validar_cep(self):
        cep_service = CEPService()
        dados_cep = cep_service.buscar_por_cep(self.cep)

        if not dados_cep:
            self.observacoes.append("CEP inválido")
            self.endereco = {}
        else:
            self.endereco = {
            "logradouro": dados_cep.get("logradouro", ""),
            "bairro": dados_cep.get("bairro", ""),
            "cidade": dados_cep.get("localidade", ""),
            "uf": dados_cep.get("uf", "")
        }
    

