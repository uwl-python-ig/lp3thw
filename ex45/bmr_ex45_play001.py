from bmr_ex45_regions import *
from bmr_ex45_creatures import *
from textwrap import dedent

grass = Grasslands()
mountain = Mountains()

unicorn = Unicorn()
troll = Troll()

regions = [grass, mountain]

'''
this var caused the two creature methods to run before begin()...why!?

encounters = {
    'unicorn': unicorn.encounter() ,
    'troll': troll.encounter() 
}
'''

present_location = 'NOT_SET'

def begin():
    print(f"""\nBMR_EX45
    {'=' * 20}
    These are the regions:
    """)
    for region in regions:
        print(f"{region.appellation}: {region.description}")
    print("\nWhere will you begin your journey? Enter a number.")
    for region in regions:
        print(f"{regions.index(region) + 1}: {region.appellation}")
    start = int(input("> "))
    print(f"You start your journey in {regions[start - 1].appellation}...")
    present_location = regions[int(start - 1)]

begin()
