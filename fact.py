def main():
    print fact_loop(4)
# added note 

def fact_loop(d):
    fact = 1
    for i in range(1,d+1):
        fact = fact * i
    return fact

if __name__ == "__main__":
    main()
# added another note