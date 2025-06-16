# hello.py
# In order to compile hello.py, please navigate to where hello.py belongs, then launch the following command:
# python scripts/hello.py
# This a script named hello with the extension .py which is a module. Enconding = UTF-8

"""
    A little script that shows how to write clean code via a main function
    It shows a little example about the usage of the print function ...
"""



def main() -> None:
    """
        @params: None
        @returns: None
        ... description ...
    """
    print("Hello World!")

    my_str : str = "Hello World!"

    print(my_str)


if __name__ == "__main__":
    main()
