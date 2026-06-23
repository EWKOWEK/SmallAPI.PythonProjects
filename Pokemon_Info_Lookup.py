import requests
import json

def ChooseYourPokemon(Choice=None):
    if Choice is None:
        Choice = input("Enter the name or ID of the Pokemon you want info about: ")
    url = f"https://pokeapi.co/api/v2/pokemon/{Choice.lower()}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        name = data['name']
        id = data['id']
        height = data['height']
        weight = data['weight']
        types = [t['type']['name'] for t in data['types']]
        
        print(f"Name: {name.capitalize()}")
        print(f"ID: {id}")
        print(f"Height: {height}")
        print(f"Weight: {weight}")
        print(f"Types: {', '.join(types)}")
        showAbilities = input("Do you want to see the abilities of this Pokemon? (y/n): ")
        if showAbilities.lower() == 'y':
            abilities = []
            for a in data['abilities']:
                abilityName = a['ability']['name']
                abilities.append(abilityName)
            for x, ability in enumerate(abilities, start=1):
                print(f"{x}) {ability}")
        else: 
            print("Abilities not displayed.")
        showMoves = input("Do you want to see the moves of this Pokemon? (y/n): ")
        if showMoves.lower() == 'y':
            moves = []
            for m in data['moves']:
                move_info = m['move']          
                move_name = move_info['name']                 
                moves.append(move_name)
            for x, move in enumerate(moves, start=1):
                print(f"{x}) {move}")
        else:
            print("Moves not displayed.")
    else:
        print(f"Error: Pokemon not found. Please check the name or ID and try again.")

Choice = input("Enter the name or ID of the Pokemon you want info about: ")
ChooseYourPokemon(Choice)