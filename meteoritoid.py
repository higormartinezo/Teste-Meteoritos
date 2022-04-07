#Meteorito ID
#Criado por Higor Martinez Oliveira
#martinezoliveirahigor@gmail.com

print("\nTeste se uma rocha pode ter vindo do espaço!")
print("\nEste programa verifica se uma rocha pode ser um meteorito.\nPara isso, responda algumas perguntas sobre as características que ela possui.\nPara cada pergunta responda S para sim ou N para não.")
        
print("\nVamos começar!")

def meteoritoID():
        a = input("\nA rocha é atraída por ímã? ")
        while (a.upper() != "S" and a.upper() != "N"):
                print("Entrada inválida\n")
                a = input("A rocha é atraída por ímã? ")
        b = input("\nEla é mais pesada do que uma rocha de tamanho parecido? ")
        while (b.upper() != "S" and b.upper() != "N"):
                print("Entrada inválida\n")
                b = input("Ela é mais pesada do que uma rocha de tamanho parecido? ")
        
        if (a.upper() == "N" and b.upper() == "S") or (a.upper() == "S" and b.upper() == "N"):
                print("\nINFELIZMENTE NÃO DEVE SER UM METEORITO!")
                return refazer()
        elif a.upper() == "N" and b.upper() == "N":
                c = input("\nEla tem uma fina crosta escura por fora que destaca do interior? ")
                while (c.upper() != "S" and c.upper() != "N"):
                        print("Entrada inválida\n")
                        c = input("Ela tem uma fina crosta escura por fora que destaca do interior? ")
                if c.upper() == "N":
                        print("\nINFELIZMENTE NÃO DEVE SER UM METEORITO!")
                        return refazer()
                if c.upper() == "S":
                        d = input("\nO interior é claro? ")
                        while (d.upper() != "S" and d.upper() != "N"):
                                print("Entrada inválida\n")
                                d = input("O interior é claro? ")
                        if d.upper() == "N":
                                print("\nINFELIZMENTE NÃO DEVE SER UM METEORITO!")
                                return refazer()
                        if d.upper() == "S":
                                print("\nPODE SER UM METEORITO!\nEnvie fotos da rocha suspeita para análise: meteoritoid@gmail.com")
                        
        elif (a.upper() == "S" and b.upper() == "S"):
                e = input("\nO interior é todo prateado como aço inox ou tem pintinhas prateadas? ")
                while (e.upper() != "S" and e.upper() != "N"):
                        print("Entrada inválida\n")
                        e = input("O interior é todo prateado como aço inox ou tem pintinhas prateadas? ")
                if e.upper() == "N":
                        print("\nINFELIZMENTE NÃO DEVE SER UM METEORITO!")
                        return refazer()
                if e.upper() == "S":
                        f = input("\nTem uma fina crosta escura por fora que destaca do interior? ")
                        while (f.upper() != "S" and f.upper() != "N"):
                                print("Entrada inválida\n")
                                f = input("Tem uma fina crosta escura por fora que destaca do interior? ")
                        if f.upper() == "N":
                                print("\nINFELIZMENTE NÃO DEVE SER UM METEORITO!")
                                return refazer()
                        if f.upper() == "S":
                                print("\nPODE SER UM METEORITO!\nEnvie fotos da rocha suspeita para análise: meteoritoid@gmail.com")
                                
def refazer():
        r = input("Deseja refazer o teste? ")
        if r.upper() == "S":
                return meteoritoID()
        else:
                return None

meteoritoID()
