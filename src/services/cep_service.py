import requests

class CEPService:
    def buscar_por_cep(self, cep: str) -> dict:
        cep = cep.replace("-", "").strip()
        url = f"https://viacep.com.br/ws/{cep}/json/"

        try:
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                dados = response.json()
                if "erro" in dados:
                    return {}
                return dados
        except requests.RequestException:
            pass

        return {}

