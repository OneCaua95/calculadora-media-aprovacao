primeira_nota = float(input("Digite a primeira nota:"))
segunda_nota = float(input("Digite a segunda nota:"))
terceira_nota = float(input("Digite a terceira nota:"))

def Media(primeira_nota, segunda_nota, terceira_nota):
    return (primeira_nota + segunda_nota + terceira_nota) / 3

def Media_final(primeira_nota, segunda_nota, terceira_nota, nota_recuperacao):
    numerador = (primeira_nota * 0.6) + (segunda_nota * 0.6) + (terceira_nota * 0.6) + (nota_recuperacao * 0.4)
    denominador = 0.6 * 3 + 0.4
    return numerador / denominador

media_nota = Media(primeira_nota, segunda_nota, terceira_nota)

if media_nota >= 7.0:
    print(f"aluno aprovado, sua média é {media_nota}")
elif media_nota < 4.0:
    print(f"aluno reprovado, sua média é {media_nota}")
else:
    print(f"você não foi aprovado pela média das três avaliações, como sua média é {media_nota} por ser maior que 4 você tem direito a uma prova de recuperação.")
    nota_recuperecao = float(input("Digite a nota de recuperação:"))
    media_final = Media_final(primeira_nota, segunda_nota, terceira_nota, nota_recuperecao)
    if media_final >= 5.0:
        print(f"aluno aprovado, sua média final é de {media_final}")
    else:
        print(f"aluno reprovado, sua média final é {media_final}")
