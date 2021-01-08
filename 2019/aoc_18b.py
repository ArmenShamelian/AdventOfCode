import numpy as np

# Globals
directions = [(-1, 0),
              (1, 0),
              (0, -1),
              (0, 1)]
key_chars = [chr(x) for x in range(ord('a'), ord('z') + 1)]
door_chars = [chr(x) for x in range(ord('A'), ord('Z') + 1)]
blocked_chars = door_chars + ['#']
key_pos = None
door_pos = None
counter = 0
key_to_key = {}
path_cache = {}
cache_calls = 0
global_optimum = np.inf


def load_input():
    file = open('input_18b.txt', 'r')
    input_ = file.read()
    return input_

# Make a map out of the input
def build_map(input_):
    map_ = {}
    x = 0
    y = 0
    starts = {}
    keys = {}
    doors = {}
    global key_chars
    global door_chars
    robot_no = 0
    for i, c in enumerate(input_):
        if c == '\n':
            y += 1
            x = 0
            continue
        else:
            map_[(x, y)] = c
            if c == '@':
                starts[robot_no] = (x, y)
                robot_no += 1
            if c in key_chars:
                keys[(x, y)] = c
            elif c in door_chars:
                doors[(x, y)] = c
            x += 1
    global key_pos
    global door_pos
    key_pos = keys
    door_pos = doors
    return map_, starts, keys, doors


def blocked(c):
    global blocked_chars
    return c in blocked_chars


def iskey(c):
    global key_chars
    return c in key_chars


def neighbors(position, map_):
    """
    Return accessible neighbors from current position.
    :param position: starting position
    :param map_: current map, with updated keys and doors
    :return: Coordinates of four neighbors.
    """
    global directions
    for i, d in enumerate(directions):
        neighbor = tuple([position[0] + d[0], position[1] + d[1]])
        if not blocked(map_[neighbor]):
            yield neighbor


def open_door(map_, key):
    door = key.upper()
    global key_pos
    global door_pos

    for pos in key_pos:
        if map_[pos] == key:
            map_[pos] = '.'

    for pos in door_pos:
        if map_[pos] == door:
            map_[pos] = '.'

    return map_

def draw_map(map_, position):
    screen = ''
    max_x = len(set([a for a, b in map_.keys()]))
    max_y = len(set([b for a, b in map_.keys()]))
    for y in range(max_y):
        for x in range(max_x):
            if (x, y) == position:
                screen += '@'
            else:
                screen += map_[(x, y)]
        screen += '\n'
    print(screen)

def iterate_bfs(map_, starts, keys, prev_steps, path=[], fromkey='@'):
    """

    :param map_: Dict of (x,y) --> character at that position
    :param starta: Positions where the four robots start
    :param keys: All positions of currently uncollected keys
    :param prev_steps: Minimum amount of steps made to get to current start from initial start.
    :return: Fewest steps to get all keys
    """

    global counter
    global cache_calls
    counter += 1
    if counter % 1000 == 0:
        print(f"Counter: {counter}, cache call index: {round(cache_calls/counter, 2)}")

    # If done: break.
    if not keys:
        return prev_steps, path

    # Use from cache if possible
    # Check if remaining path from start till end is in cache.
    key_str = list(keys.values())
    key_str.sort()
    positions = list(starts.values())
    positions.sort()
    key_str = positions + key_str
    key_str = str(key_str)
    # Check if your remaining keys are all in cache
    if key_str in key_to_key.keys():
        cache_calls += 1
        current_solution = prev_steps + key_to_key[key_str]
        return current_solution, path[:-1] + path_cache[key_str]

    # If not done, and not cached: compute new route.
    # Make a new map, with the new found key and its corresponding door opened. Only if keys are left
    map_ = map_.copy()
    map_ = open_door(map_, fromkey)

    # Keep track of keys that can be found from here.
    keys_found = {}
    # Keep track of visited nodes and number of steps required to reach them.
    visited = {}
    for robot in starts:
        visited[starts[robot]] = [0, robot]
    queue = []
    for robot in starts:
        start = starts[robot]
        for neighbor in neighbors(start, map_):
            queue.append(neighbor)
            # Track which robot visited each node.
            visited[neighbor] = [1, robot]

    # Keep traversing neighbors while there are unvisited neighbors.
    while queue:
        position = queue.pop(0)
        steps, robot = visited[position]
        for neighbor in neighbors(position, map_):
            # If this neighbor is not yet visited, add to queue.
            if neighbor not in visited.keys():
                queue.append(neighbor)
                visited[neighbor] = [steps + 1, robot]
        if position in keys.keys():
            keys_found[position] = [map_[position], robot]
            # Stop if all keys are found
            if len(keys_found) == len(keys):
                break
        # draw_map(map_, position)

    # For each key found, repeat the algorithm, until all keys have been found.
    min_steps = np.inf
    best_path = None
    for pos in keys_found.keys():
        key, robot = keys_found[pos]
        new_keys = keys.copy()
        del new_keys[pos]
        steps_until_here = visited[pos][0]
        new_prev = prev_steps + steps_until_here
        # If suboptimal: break early.
        global global_optimum
        if new_prev + len(keys_found) >= global_optimum:
            key_to_key[key_str] = np.inf
            path_cache[key_str] = ['-']
            return np.inf, path + [key]
        # Update position of moved robot
        new_starts = starts.copy()
        new_starts[robot] = pos
        steps_this_route, this_path = iterate_bfs(map_, new_starts, new_keys, new_prev, path=path+[key], fromkey=key)
        if steps_this_route <= min_steps:
            min_steps = steps_this_route
            best_path = this_path
            # If also global optimum: update it too.
            if min_steps <= global_optimum:
                global_optimum = min_steps

    # Update cache
    key_to_key[key_str] = min_steps - prev_steps
    start_index = 0 if fromkey == '@' else best_path.index(fromkey)
    path_cache[key_str] = best_path[start_index:]

    return min_steps, best_path


# Execute 18b
def run_b():
    input_ = load_input()
    map_, starts, keys, doors = build_map(input_)
    min_steps, best_path = iterate_bfs(map_, starts, keys, 0)
    print(f"Best path: {best_path}")
    return min_steps

answer = run_b()
print(answer)

