def Spatnovazbova(A,B,C,P,k,r1,r2):
    X=[0.0]
    Y=[]
    U=[]
    E=[]
    R=[]
    ustalenie=0
    ustaleny=False

    for i in range(k):
        if i <k/2:
            r=r1
            R.append(r)
        else:
            r=r2
            R.append(r)

        y=float(C*X[i])
        Y.append(y)
        e=float(Y[i]-r)
        E.append(e)
        u=float(P*e)
        U.append(u)
        x=float(A*X[i]+B*U[i])
        X.append(x)

        if i > 0 and abs(float(Y[i])-float(Y[i-1])) < 0.00001:
            ustalenie += 1
        else:
            ustalenie = 0
        if ustalenie >= 5 and not ustaleny:
            print(f"Ustálenie dosiahnuté v kroku {i-4}")
            ustaleny=True
            odchylka=sum(E[i-j] for j in range(5))/5
            print(f"Trvalá regulačná odchýlka: {odchylka}")
        if i==k/2:
            ustaleny=False
            ustalenie=0
    tabulka=[[i,'{:.10}'.format(X[i]),'{:.10}'.format(Y[i]),'{:.10}'.format(R[i]),'{:.10}'.format(E[i]),'{:.10}'.format(U[i])] for i in range(k)]
    return tabulka

def Uloz(tabulka):
    with open("Vysledky.txt", "w") as file:
        prvy="{:^5}{:^16}{:^15}{:^5}{:^15}{:^15}\n".format("k", "x(k)", "y(k)", "r(k)", "e(k)", "u(k)")
        file.write(prvy)
        for riadok in tabulka:
            file.write("{:^5}{:^15}{:^15}{:^5}{:^15}{:^15}\n".format(*riadok))


A=0.01
B=0.8
C=0.5
P=2.0
k=300
r1=2.5
r2=-1.3

tabulka=Spatnovazbova(A, B, C, P, k, r1, r2)
Uloz(tabulka)
