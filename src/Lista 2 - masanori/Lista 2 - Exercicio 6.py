gph = int(input('ganho por hora: '))
htpm = int(input('quantidade de horas trabalhadas por mes: '))
salariobruto =  gph * htpm
ir = salariobruto * 11 / 100
inss = salariobruto * 8 / 100
sindicato = salariobruto * 5 / 100
impostos = ir + inss + sindicato
sliquido = salariobruto - impostos
print('salario bruto é igual a {:.1f} reais'.format(salariobruto))
print('ir igual a {:.1f} reais'.format(ir))
print('inss é igual a {:.1f} reais'.format(inss))
print('sindicato é igual a {:.1f} reais'.format(sindicato))
print('salario liquido é igual a {:.1f} reais'.format(sliquido))
