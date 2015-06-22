import os
from .tools import make

class Builder:
    def __init__(self,args=None):
        self.args = args

    def discover(self,folder=None):
        """Check the current folder for a project to build"""
        current_dir = os.getcwd()
        if folder != None and folder != current_dir:
            self.args.remove(folder)
            os.chdir(folder)
        if len(self.args) > 1:
            self.args = self.args[1:]
        folder_items = os.listdir(folder)
        for item in folder_items:
            # Check for project files to know what to build
            if item == "Makefile":
                make(self.args)
                break
        # Return back to the original folder
        os.chdir(current_dir)
