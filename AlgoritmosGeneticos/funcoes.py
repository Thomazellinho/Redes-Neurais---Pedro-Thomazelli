def funcao_objetivo_cb(individuo):
    """ Computa a função objetivo no problema das cb.
    
    Args:
        indivíduo: lista contendo os genes da cb.
    
    Return:
        Um valor que representa as somas
    """
    return sum(individuo) 
