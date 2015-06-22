from .run import run
def main(args):
    """Build the project with the Makefile"""
    if args:
        run('make {}'.format(args))
    else:
        run('make')
