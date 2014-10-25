def main():
    n=int(input("Dati numarul de zile ="))
    if(n<0):
        print("Dati un numar mai are decat 1")
        main()
    else:
        age=n//365
        print("Persoana are ",age,"ani")
main()