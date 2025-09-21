# Crie um programa que solicite ao usuário três notas e calcule a média aritmética delas

nota1 = float(input('Qual sua primeira nota? '))
nota2 = float(input('Qual sua segunda nota? '))
nota3 = float(input('Qual sua terceira nota? '))
media = (nota1 + nota2 + nota3) / 3
media_formatada = f'{media:.2f}'
if media >= 7:
    print(f'Sua média foi {media_formatada} está aprovado!!')
else:
    print(f'Sua média foi {media_formatada} você reprovou.')