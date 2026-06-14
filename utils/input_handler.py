def get_user_input():
    print("\n🌾 Crop Yield Calculator 🌾")

    crop = input("Enter crop name (wheat/rice/maize): ").strip()
    land_size = float(input("Enter land size (in acres): "))

    return crop, land_size