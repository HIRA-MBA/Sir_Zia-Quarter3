"""Write a program that continually reads in mass from the user and then outputs the equivalent energy using Einstein's mass-energy equivalence formula (E stands for energy, m stands for mass, and C is the speed of light:"""
def main():
    mass=float(input("Enter mass of object in Kgs  "))
    energy=mass*(299792458*299792458)
    print(f"The Energy equivalent of {mass} kg is {energy} joules")


if __name__=="__main__":
    main()