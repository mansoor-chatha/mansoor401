def snow(temp):
    """This function simulates a snowfall based on the temperature."""
    if temp > 30:
        print("The weather is hot.")
    elif temp >= 25:
        print("The weather is sunny.")
    elif temp < 0:
        print("There would be a snowfall.")
    else:
        print("The weather is cool.")

def main():
    """Main function to get temperature input and call the snow function."""
    try:
        temp = float(input("Enter the temperature: "))
        snow(temp)
    except ValueError:
        print("Please enter a valid number for the temperature.")

if __name__ == "__main__":
    main()
