def main():
    farenheit=float(input("\n enter temperture in Farenheit ==> "))
    celsius:float= (farenheit -32)*(5/9)
    degree_sign = "\u00B0"
    print(f"\n{farenheit} {degree_sign}F == {degree_sign}{celsius}C")



if __name__ == "__main__":
    main()