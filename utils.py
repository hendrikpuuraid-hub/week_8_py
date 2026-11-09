my_list = ['Batman \n', 'Elsa\n', 'Wonder Woman  \n', 'Spider-Man  \n', 'Iron Man  \n', 'Superman  \n', 'Captain Marvel  \n', 'Harry Potter']

def clean_my_list(my_list):
    ''' 
    Puhastab antud nimekirja elementide ja lopust tuhikud ning reavahed
    '''
    
    cleaned_list = []

    for element in my_list:
        clean_element = element.strip()
        cleaned_list.append(clean_element)

    return cleaned_list
