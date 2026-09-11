
def approximation_pi(n):
    if n < 0 :
        print("Le nombre d'approximations doit être un entier positif.")
        return
    pi_approx = 3
    print(f"Approximation 1 : {pi_approx}")

    signe = 1
    for i in range(1, n):
        d = 2*i
        terme = 4 / (d*(d+1)*(d+2))
        pi_approx += signe * terme
        print(f"Approximation {i+1} : {pi_approx}")
        signe *= -1
if __name__ == "__main__":
    try :
        N=int(input("Entrer le nombre d'approximations voulues : "))
        approximation_pi(N)
    except ValueError :
        print("Entrer un nombre entier positif.")