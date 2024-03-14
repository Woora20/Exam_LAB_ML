def simple_poet(p):
    with open(p, "r") as f:
        lines = f.read().splitlines()

    return lines

if __name__ == '__main__':
    res = simple_poet('poem.txt')
    print(res)

# Output
# ['Where the departed goes, by Student', '', 'Where herons go', 'is a place for a departed soul.',
#   'What the choirs say', 'is how soul not just go away.', 'Like an origami,',
#     'it just shifts to a new story.', 'Transform the end of an old', 'to the beginning of a new fold.']