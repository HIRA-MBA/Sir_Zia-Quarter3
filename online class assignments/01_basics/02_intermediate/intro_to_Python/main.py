def main():
    # Define gravity constants
    gravity_constants = {
        "Mercury": 0.376,
        "Venus": 0.889,
        "Mars": 0.378,
        "Jupiter": 2.36,
        "Saturn": 1.081,
        "Uranus": 0.815,
        "Neptune": 1.14
    }

    try:
        # Prompt for Earth weight
        earth_weight = float(input("Enter your weight on Earth (kg): "))

        # Prompt for planet name and format it
        planet = input("Enter a planet name: ").capitalize()

        # Check if planet is valid
        if planet in gravity_constants:
            gravity = gravity_constants[planet]
            planetary_weight = earth_weight * gravity
            print(f"\nThe equivalent weight on {planet} is: {planetary_weight:.2f} kg")
        else:
            print("Invalid planet name. Please choose from Mercury, Venus, Mars, Jupiter, Saturn, Uranus, or Neptune.")

    except ValueError:
        print("Please enter a valid number for weight.")

if __name__ == "__main__":
    main()

