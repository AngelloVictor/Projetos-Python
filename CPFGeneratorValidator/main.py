import random

first_dig_validate = [10, 9, 8, 7, 6, 5, 4, 3, 2]
second_dig_validade = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2]
num_cpf = [4,5,4,4,4,3,3,9,8,3,8]
aux_num_cpf_first = []
aux_num_cpf_second = []
print(num_cpf)


def cpf_validate(cpf):

    # Verifica se o cpf tem 11 digitos
    if len(cpf) > 11:
        print("CPF Invalido")

    else:
        # Valida primeiro digito
        for i in range(9):
            aux_num_cpf_first.append(cpf[i] * first_dig_validate[i])


        # Valida segundo digito
        for i in range(10):
            aux_num_cpf_second.append(cpf[i] * second_dig_validade[i])

        expected_first_dig = 11 - (sum(aux_num_cpf_first) % 11)
        expected_second_dig = sum(aux_num_cpf_second) % 11
        
        if cpf[9] != expected_first_dig or cpf[10] != expected_second_dig:
            print("CPF Invalido")
            
        else:
            print("CPF Valido")        
        
        
        
cpf_validate(num_cpf)

# Retorna o CPF
#cpf = str("".join(str(num) for num in num_cpf))
#cpf = cpf.zfill(11)
#print(f"CPF: {cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:11]} or {cpf}")
