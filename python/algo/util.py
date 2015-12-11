import os.path


def test_data(module):
    name = os.path.splitext(os.path.basename(module))[0]
    return '/Users/evgeny/Downloads/rosalind_%s.txt' % name