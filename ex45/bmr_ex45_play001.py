from bmr_ex45_regions import *
from textwrap import dedent

# set these in _regions?
grass = Grasslands()
mountain = Mountains()

regions = [grass, mountain]

print(dedent(f"""\nBMR_EX45
{'=' * 20}
"""))

print("These are the regions:")
for region in regions:
    print(f"{region.appellation}: {region.description}")

print("\nWhere will you begin your journey? Enter a number.")

for region in regions:
    print(f"{regions.index(region) + 1}: {region.appellation}")

start = int(input("> "))

print(f"You start your journey in {regions[start - 1].appellation}...")
