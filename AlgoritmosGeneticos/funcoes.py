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

def populacao_cb(tamanho, n):
    '''Cria uma população no problema das caixas binárias.
    
    Args: 
        Tamanho: da população
        n: número de genes
        
    Return:
        Lista na qual cada item é um indivíduo, sendo esse uma lista com n genes'''
    populacao = []
    for _ in range (tamanho):
        populacao.append(individuo_cb(n))
    return populacao


def selecao_roleta_max(populacao, fitness):
    '''Seleciona indivíduos de uma população usando o método da roda. (Funciona apena para problemas de maximização
    
    Args:
        populacao: lista com todos os indivíduos que serão selecionados
        fitness: lista com o valor da função objetivo dos inviduos da populacao
    
    Return:
        População de indivíduos selecionados.
    '''
    
    populacao_selecionada = random.choices(populacao, weights = fitness, k = len(populacao))
    return populacao_selecionada

def funcao_objetivo_cb(individuo):
    """ Computa a função objetivo no problema das cb.
    
    Args:
        indivíduo: lista contendo os genes da cb.
    
    Return:
        Um valor que representa as somas
    """
    return sum(individuo) 

def funcao_objetivo_pop_cb(populacao):
    ''' Calcula a função objetivo para todos os membros de uma população.
    
    Args:
        populacao: lista com todos os individuos da populacao
    
    Return:
        lista de valores representando a fitness de cada individuo da popualçao
        
    ''' 
    fitness = []
    for individuo in populacao:
        fobj = funcao_objetivo_cb(individuo)
        fitness.append(fobj)
    return fitness