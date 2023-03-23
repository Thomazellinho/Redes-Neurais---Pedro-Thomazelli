import random


def gene_cb ():
    """ Gerar um gene válido para o problema apresentado
    
    Return:
        Valor 0 ou 1.
    """
    lista = [0,1]
    gene = random.choice(lista)
    return gene

def gene_cnb (valor_max_caixa):
    ''' Gerar um gene válido para o problema apresentado, agora variando de 0 a 100.
    
    Args:
        valor_max_caixa: valor máximo que a caixa pode assumir.
        
    Return:
        valor de 0 a 100 (inclusive).
    '''
    gene = random.randint(0, valor_max_caixa)
    return gene

def individuo_cnb(numero_genes, valor_max_caixa):
    """ Gera um individuo válido para o problema.
    
    Args:
        numero_genes: número de genes na lista que representa o indivíduo
        valor_max_caixa: valor máximo que a caixa pode assumir
    
    Return:
        Uma lista representando um indivíduo válido para o problemada CNB
    """
    individuo = []
    for _ in range(numero_genes):
        gene = gene_cnb(valor_max_caixa)
        individuo.append(gene)
    return individuo

def populacao_cnb(tamanho_populacao, numero_genes, valor_max_caixa):
    '''Cria uma população de indivíduos para o problema das caixas não-binárias
    
    Args:
        tamanho_populacao: numero de individuos
        numero_genes: número de genes na lista, representando o indivíduo
        valor_max_caixa: valor máximo que a caixa pode assumir
    
    Return:
        Uma lista com cad aitem representando um indivíduo
    '''
    
    populacao = []
    for _ in range(tamanho_populacao):
        individuo = individuo_cnb(numero_genes, valor_max_caixa)
        populacao.append(individuo)
    return populacao

def funcao_objetivo_cnb(individuo):
    ''' calcula o fitness do individuo para o problema das cnb.
    
    Args:
        individuo: lista que representa uma individuo
        
    Return:
        valor representando o fitness do individuo
    '''
    fitness = sum(individuo)
    return fitness

def funcao_objetivo_pop_cnb(populacao):
    '''calcula o fitness da população completa
    
    Args:
        populacao: lista com todos os individuos
        
    Return:
        lista com o fitness de cada individuo em ordem
    '''
    fitness_pop = []
    for individuo in populacao:
        fitness_ind = funcao_objetivo_cnb(individuo)
        fitness_pop.append(fitness_ind)
    return fitness_pop

def mutacao_cnb(individuo, valor_max_caixa):
    ''' faz a mutação
    
    Args:
        individuo: individuo que deve sofrer a mutaçao
        valor_max_caixa: valor máximo que a caixa pode assumir
        
    Return:
        individuo mutado
    '''
    gene_a_ser_mutado = random.randint(0, len(individuo) - 1)
    individuo[gene_a_ser_mutado] = gene_cnb(valor_max_caixa)
    return individuo
    
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

def cruzamento_ponto_simples(mae, pai):
    ''' Operador de cruzamento de ponto simples.
    
    Args:
        pai: uma lista representando um indivíduo
        mãe: uma lista representando um indivíduo
    
    Return:
        Duas listas, cada uma representando um filho dos pais que foram colocados como argumento
        
    '''
    ponto_de_corte = random.randint(1, len(pai) - 1)
    filho1 = pai[:ponto_de_corte] + mae[ponto_de_corte:]
    filho2 = mae[:ponto_de_corte] + pai[ponto_de_corte:]
    
    return filho1, filho2

def mutacao_cb(individuo):
    '''Realiza a mutação de um gene no problema das caixas binárias
    
    Args:
        indivíduo: uma lista representando um indivíduo no problema das caixas binárias
        
    Return:
        Um indivíduo com o gene mutado.
    
    '''
    gene_a_ser_mutado = random.randint(0, len(individuo)-1)
    individuo[gene_a_ser_mutado] = gene_cb()
    return individuo

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