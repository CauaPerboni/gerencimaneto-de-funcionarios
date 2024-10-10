from funcionario import Funcionario

def preencher_dados_funcionario():
    nome = input("Digite o nome do funcionário: ")
    email = input("Digite o email do funcionário: ")
    funcionario = Funcionario(nome, email)
    
    while True:
        mes = input("Digite o mês para cadastrar horas (ou 'sair' para encerrar): ")
        if mes.lower() == 'sair':
            break
        horas = float(input(f"Digite as horas trabalhadas em {mes}: "))
        funcionario.cadastro_hora(mes, horas)

        salario_hora = float(input(f"Digite o salário por hora em {mes}: "))
        funcionario.cadastro_salario_hora(mes, salario_hora)
    
    return funcionario

def main():
    funcionario = preencher_dados_funcionario()
    print("\nResumo dos dados cadastrados:")
    print(funcionario)
    print("\nSalários calculados: ")
    funcionario.resumo_salarios()
    print("                 ")

if __name__ == "__main__":
    main()
