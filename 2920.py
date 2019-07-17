# Print one of ascending, descending, or mixed on the first line.

import sys

notes = list(map(int, sys.stdin.readline().split()))

ascending_notes = sorted(notes)
descending_notes = sorted(notes, reverse=True)

if notes == ascending_notes:
    print('ascending')
elif notes == descending_notes:
    print('descending')
else:
    print('mixed')
