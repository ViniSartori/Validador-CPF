import sys

cpf = input('Digite seu CPF: ').replace('.', '').replace('-', '')

sequencial = cpf == cpf[0] * len(cpf)
if sequencial:
    print('Você enviou dados sequenciais')
    sys.exit()

nove_digitos = cpf[:9]
contador_regressivo_1 = 10

resultado_digito_1 = 0
for digito in nove_digitos:
    resultado_digito_1 += int(digito) * contador_regressivo_1
    contador_regressivo_1 -= 1

primeiro_digito = (resultado_digito_1 * 10) % 11
primeiro_digito = primeiro_digito if primeiro_digito <= 9 else 0

dez_digitos = str(nove_digitos) + str(primeiro_digito)
contador_regressivo_2 = 11

resultado_digito_2 = 0
for digito_2 in dez_digitos:
    resultado_digito_2 += int(digito_2) * contador_regressivo_2
    contador_regressivo_2 -= 1

segundo_digito = (resultado_digito_2 * 10) % 11
segundo_digito = segundo_digito if segundo_digito <= 9 else 0

cpf_calculado = str(dez_digitos) + str(segundo_digito)

if cpf_calculado == cpf:
    print('CPF validado')
else:
    print('Você digitou um CPF inválido')
