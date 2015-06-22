from subprocess import Popen, PIPE
def run(args):
    """Run the build command in the shell"""
    try:
        with Popen(args,stdout=PIPE,stderr=PIPE) as process:
            out, err = process.communicate()
            print(out[:-1].decode('utf8'))
            if err:
                print(err.decode('utf8'))
    except OSError as e:
        print('OS Error: {}'.format(e))
        return False
    except FileNotFoundError as e:
        print('File not found: {}'.format(e))
    except ValueError as e:
        # invalid arguements
        print('Invalid arguments for {0}'.format(args))
