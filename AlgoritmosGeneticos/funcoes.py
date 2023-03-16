import random


def gene_cb ():
    """ Gerar um gene válido para o problema apresentado
    
    Return:
        Valor 0 ou 1.
    """
    lista = [0,1]
    gene = random.choice(lista)
    return gene

def individuo_cb(n):
    """ Gerar um indivíduo para o problema apresentado.
    
    Args:
        n: número de genes do indivíduo.
    
    Return:
        lista com "n" genes, com valor 0 ou 1.
    """
    individuo = []
    for i in range(n):
        gene = gene_cb()
        individuo.append(gene)
    return individuo

def funcao_objetivo_cb(individuo):
    """ Computa a função objetivo no problema das cb.
    
    Args:
        indivíduo: lista contendo os genes da cb.
    
    Return:
        Um valor que representa as somas
    """
    return sum(individuo) 