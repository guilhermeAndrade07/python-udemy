alunos = ['Guilherme', 'Joaquim', 'Carlos', 'Gobato', 'Marcel']
notas = [10, 5, 8, 3, 9]
resultado = list(zip(alunos, notas))

for aluno, nota in resultado:
    print(f'{aluno}: {nota}')