import chess
import itertools
from two_player import play_game
from paranoid_king_v1 import paranoid_king as pkv1
from Engines import engine_random 


engines = [pkv1,engine_random]

def permute_players(num_matches):
    """Plays the whole tournament. Each engine against each other. Even against the same one."""
    # Modify it if there is a game, either to skip it, or add to the previous list. Can pass this as a parameter. 
    player_list = []
    matches_played = []
    with open("filename.txt", "r") as file:
        # lines = file.readlines()
        for line in file:
            if(line.strip()):
                matches_played.append((line.strip().split())[:2])
    for played in matches_played:   
        played[0], played[1] = getattr(engines, played[0]),getattr(engines, played[1])
    matches_played = [(el[0], el[1]) for el in matches_played]
    with open('engine_list.txt', 'r') as file:
        for line in file:
            player_list.append(getattr(engines, line.strip()))
    matches = list(itertools.product(player_list, repeat=2))
    for match in matches:
        should_continue = 0
        for el in matches_played:
            if(match == el):
                # print("skipping rally", el)
                should_continue = 1
                break
        if(should_continue): continue
        play_game(match[0], match[1],num_matches)
permute_players(1)
