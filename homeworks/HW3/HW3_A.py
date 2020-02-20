#Amina Muumin, muumi002, lab 008, HW3A
def CMYK_to_RGB(C,M,Y,K):
    C/= 100
    M/= 100
    Y/= 100
    K/= 100
    R = 255 * (1-C) * (1-K)
    G = 255 * (1-M) * (1-K)
    B = 255 * (1-Y) * (1-K)
    R = int(round(R))
    G = int(round(G))
    B = int(round(B))
    return [R,G,B]

def main():
    C = int(input("Cyan component: "))
    M = int(input("Magenta component: "))
    Y = int(input("Yellow component: "))
    K = int(input("Black component: "))
    L = CMYK_to_RGB(C,M,Y,K)
    print ("RGB representation: ", L[0], L[1], L[2])

if __name__ == "__main__":
    main() 
