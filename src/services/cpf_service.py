def validar_cpf(cpf: str) -> bool:
    """
    Valida o CPF considerando os dígitos verificadores.
    Espera o CPF com apenas dígitos (sem pontos ou hífen).
    """
    cpf = ''.join(filter(str.isdigit, cpf))

    if len(cpf) != 11 or cpf == cpf[0] * 11:
        return False

    def calc_dv(cpf_slice, peso):
        s = sum(int(d) * p for d, p in zip(cpf_slice, range(peso, 1, -1)))
        resto = (s * 10) % 11
        return 0 if resto == 10 else resto

    dv1 = calc_dv(cpf[:9], 10)
    dv2 = calc_dv(cpf[:10], 11)
    return int(cpf[9]) == dv1 and int(cpf[10]) == dv2
