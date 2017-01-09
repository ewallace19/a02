"""
    Problem:

        The function `season` should take the first three letters of the
        name of a month and print the season it is in. For this program,
        assume that Dec-Feb is winter, Mar-May is spring and so on.

        If an unknown month is entered, print "Month not recognised"

    Tests:

        >>> season("jan")
        Winter
        >>> season("feb")
        Winter
        >>> season("mar")
        Spring
        >>> season("apr")
        Spring
        >>> season("may")
        Spring
        >>> season("jun")
        Summer
        >>> season("jul")
        Summer
        >>> season("aug")
        Summer
        >>> season("sep")
        Autumn
        >>> season("oct")
        Autumn
        >>> season("nov")
        Autumn
        >>> season("dec")
        Winter
        >>> season("abc")
        Month not recognised

"""

# This code tests your solution. Don't edit it.
import doctest
def run_tests():
    doctest.testmod(verbose=True, optionflags=doctest.NORMALIZE_WHITESPACE)


def season(month):
    if month in winter(month):
        print("Winter")
    elif month in spring(month):
        print("Spring")
    elif month in summer(month):
        print("Summer")
    elif month in autumn(month):
        print("Autumn")
    else:
        print("month not recognised")

def winter(month):
    winter["dec", "jan", "feb"]

def spring(month):
    spring["mar", "apr", "may"]

def summer(month):
    summer["jun", "jul", "aug"]

def autumn(month):
    autumn["sep", "oct", "nov"]

    
