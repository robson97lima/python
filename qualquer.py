def emprestimo(idade, valor_emprestimo, salario, quantidade_parcelas):
    if idade < 22 or idade > 55 or valor_emprestimo < 1000 or valor_emprestimo > salario * 15 or quantidade_parcelas < 3   or quantidade_parcelas > 20:
        print("Não aceito")
    else:
        print("Aceito")

emprestimo(25, 1500, 500, 5)