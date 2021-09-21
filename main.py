def main():
    size=int(input("enter size: "))
    for i in range(size):
        for j in range(size):
            print(chr(9632+(i+j)%2), end=" ")
        print("")

if __name__=="__main__":
    main()