import os


def system_console(function):
    def wrapper(connection):
        os.system('cls')
        function(connection)
        input('')
        os.system('cls')

    wrapper.__doc__ = function.__doc__
    return wrapper
