"""Arquivo principal que será interpretado pelo interpretador."""


def main():
    """Função principal que será rodada quando o script for passado para o interpretador."""
    # COLOQUE SEU CÓDIGO AQUI
    N1 = float(input("Digite o primeiro número \n"))
    N2 = float(input("Digite o segundo número \n"))
    N3 = float(input("Digite o terceiro número \n"))

    if N1 >= N2 and N1 >= N3:
      maior = N1
    elif N2 >= N1 and N2 >= N3:
      maior = N2
    else:
      maior = N3
    
    print(f"{maior}")

if __name__ == '__main__':
    main()
