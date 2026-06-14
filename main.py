from core.pricing import get_crop
from core.calculator import calculate_profit
from utils.input_handler import get_user_input


def main():
    crop_name, land_size = get_user_input()

    crop = get_crop(crop_name)

    if not crop:
        print("\n❌ Crop not found! Available: wheat, rice, maize")
        return

    result = calculate_profit(crop, land_size)

    print("\n📊 FARM REPORT")
    print("-" * 30)

    print(f"Total Yield: {result['yield']} kg")
    print(f"Total Revenue: Rs {result['revenue']}")
    print(f"Total Cost: Rs {result['total_cost']}")
    print(f"Net Profit: Rs {result['profit']}")

    print("\n📦 Cost Breakdown:")
    for item, value in result["cost_breakdown"].items():
        print(f"{item}: Rs {value}")


if __name__ == "__main__":
    main()