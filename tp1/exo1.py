def calculer_imc() -> None:
    poids = float(input("Entrez votre poids (en kg) : "))
    taille = float(input("Entrez votre taille (en mètres, ex: 1.75) : "))

    imc = poids / (taille * taille)

    print(f"Votre Indice de Masse Corporelle (IMC) est de : {imc:.2f}")


if __name__ == "__main__":
    calculer_imc()