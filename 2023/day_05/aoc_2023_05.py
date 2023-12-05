import parse


def cut_out_of_range(original_start, original_end, cut_start, cut_end):
    remainders = []
    # Left side of cut remainder
    if original_start < cut_start:
        remainders.append((original_start, cut_start))
    # Right side of cut remainder
    if original_end > cut_end:
        remainders.append((cut_end, original_end))
    return remainders


puzzle_input_path = "input.txt"

# Parse input
with open(puzzle_input_path) as f:
    raw_puzzle_input = f.read().strip()

split_puzzle_input = raw_puzzle_input.split('\n\n')
initial_seeds = seeds = list(map(lambda s: int(s[0]), parse.findall("{:d}", split_puzzle_input[0])))
# maps structure [[(dest. range start, src. range start, range length)]]
list_of_lists_ranges = []
for src_dest_map in split_puzzle_input[1:]:
    list_of_ranges = []
    for unparsed_range in src_dest_map.split('\n')[1:]:
        parsed_range = tuple(map(lambda n: int(n), unparsed_range.split()))
        list_of_ranges.append(parsed_range)
    list_of_lists_ranges.append(list_of_ranges)

# Part 1
seeds = initial_seeds.copy()
for list_of_ranges in list_of_lists_ranges:
    next_seeds = []
    for seed in seeds:
        next_seed = seed
        for dest, src, length in list_of_ranges:
            # Does seed get a new number?
            if src <= next_seed < src + length:
                next_seed = dest + (next_seed - src)
                break
        next_seeds.append(next_seed)
    seeds = next_seeds


# Part 2
initial_seed_ranges = list(map(lambda s: (int(s[0]), int(s[0]) + int(s[1])), parse.findall("{:d} {:d}", split_puzzle_input[0])))
ranges_to_be_considered = initial_seed_ranges.copy()
for map_step in list_of_lists_ranges:
    ranges_considered = []
    while len(ranges_to_be_considered) > 0:
        original_start, original_end = ranges_to_be_considered.pop()
        cut = False
        for dest, src, length in map_step:
            cut_start = max(original_start, src)
            cut_end = min(original_end, src + length)
            # Is there even a cut to be made?
            if cut_start < cut_end:
                cut = True
                ranges_to_be_considered.extend(cut_out_of_range(original_start, original_end, cut_start, cut_end))
                mapped_cut_start = dest + (cut_start - src)
                mapped_cut_end = dest + (cut_end - src)
                ranges_considered.append((mapped_cut_start, mapped_cut_end))
        if not cut:
            ranges_considered.append((original_start, original_end))
    ranges_to_be_considered = ranges_considered

print(min(ranges_to_be_considered, key=lambda t: t[0]))
