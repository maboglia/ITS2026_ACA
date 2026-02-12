""" Analizzatore di oggetti"""

def analizza(collezione):
    """
    Docstring for analizza
    
    :param collezione: Description
    """
    print("# elementi ",len(collezione))
    print("Tipo del dato ",type(collezione))
    print("Metodi disponibili", help(collezione))