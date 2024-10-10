# Projeto: Gerenciamento de Funcionários

Este é um projeto simples em Python que permite o cadastro de funcionários, gerenciamento de horas trabalhadas e salário-hora, além do cálculo do salário para cada mês. O projeto foi desenvolvido para ser interativo, onde o usuário pode inserir os dados diretamente no terminal e obter um resumo dos salários calculados.

## Funcionalidades

- Cadastro de funcionários com nome e email.
- Registro de horas trabalhadas por mês.
- Definição do valor do salário por hora para cada mês.
- Cálculo do salário mensal com base nas horas trabalhadas e no salário por hora.
- Geração de um resumo final com todos os dados do funcionário e os salários de cada mês.

## Como usar

1. Clone o repositório:
    ```bash
    git clone https://github.com/seu-usuario/nome-do-repositorio.git
    ```

2. Navegue até o diretório do projeto:
    ```bash
    cd nome-do-repositorio
    ```

3. Execute o arquivo `teste_funcionario.py`:
    ```bash
    python teste_funcionario.py
    ```

4. Insira os dados solicitados no terminal, como nome do funcionário, email, horas trabalhadas por mês e o valor do salário por hora.

5. O programa exibirá um resumo com os dados cadastrados e os salários calculados para cada mês registrado.

## Exemplo de Execução

```bash
Digite o nome do funcionário: Fulano
Digite o email do funcionário: fulano@blablabla.com.br
Digite o mês para cadastrar horas (ou 'sair' para encerrar): Jan
Digite as horas trabalhadas em Jan: 160
Digite o salário por hora em Jan: 30
Digite o mês para cadastrar horas (ou 'sair' para encerrar): Fev
Digite as horas trabalhadas em Fev: 150
Digite o salário por hora em Fev: 28
Digite o mês para cadastrar horas (ou 'sair' para encerrar): sair

Resumo dos dados cadastrados:
Funcionário: Fulano, 
Email: fulano@blablabla.com.br, 
Horas/mês: {'Jan': 160, 'Fev': 150}, 
Salário-hora: {'Jan': 30, 'Fev': 28}

Salários calculados:
Salário de Jan: 4800
Salário de Fev: 4200
