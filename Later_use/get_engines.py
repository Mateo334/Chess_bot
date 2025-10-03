import inspect
import Later_use.engines as engines
import chess
functions = [name for name, obj in inspect.getmembers(engines, inspect.isfunction)]

# Print function names
with open("engine_list.txt", 'w') as file:
    for func in functions:
        file.write(func)
        file.write('\n')
with open("engine_list.txt", 'r') as file:
    for line in file:
        print(getattr(engines, line.strip())(chess.Board()))
        