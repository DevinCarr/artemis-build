from .main import Builder
VERSION = "0.1.0"

def execute(args=None):
    """Entry point for Artemis-core"""
    builder = Builder(args)
    if args:
        if args[0] == 'this' or args[0] == 'here':
            # Run in the current directory
            builder.discover(args[1])
        else:
            # The argument is assumed to be a folder
            builder.discover(args[0])
    else:
        # Run in the current directory
        builder.discover()

def help_message():
    """Help message for Artemis-core"""
    return "Build tool plugin (v{})".format(VERSION)
