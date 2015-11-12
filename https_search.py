import time
from pygoogle import pygoogle

def https_search(url):
   
    string_search = "inurl:https site:"+str(url)

    g = pygoogle(string_search)
    g.pages = 5
    g.hl = "br"

    print string_search 

    results_numbers = 0
    count = 0
    temp = 6 # segundos

    while results_numbers == 0 :
        results_numbers = g.get_result_count()
        print "Resultados:",results_numbers
        print
        if results_numbers == 0:
            time.sleep( temp ) 
            count += temp 
            if count > 60: # segundos
                count = -1
                print "Desisto!"
                break

    desired_results = 5
    search_sites = {}

    if count == -1:
        print "Sem estima dos resultados da pesquisa"
        return 0

    elif results_numbers < desired_results:
        print "Poucos sites!"
        desired_results = results_numbers
    
    while len(search_sites) == 0:
        search_sites = g.search()
        print search_sites
        print
        for key in search_sites.keys():
            print key, search_sites[key]
        if len(search_sites) == 0 or len(search_sites) < desired_results:
            time.sleep( temp ) 
            count += temp 
            if count > 60: # segundos
                count = -1
                print "Desisto!"
                break
    
    if count == -1:
        print "Possivel bloqueio do Google"
        return 0
   
    
    print "Fim"
