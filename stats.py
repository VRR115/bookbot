def get_book_text(file_path):
    file_contents =None
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def get_num_words(file_path):
    file_contents =None
    with open(file_path) as f:
        file_contents = f.read()
    file_number_ll = file_contents.split()
    file_number = len(file_number_ll)
    return file_number

def get_character_count(file_path):
    file_contents =None
    with open(file_path) as f:
        file_contents= f.read()

    file_characters_list = list(file_contents.lower())
    dictt ={}
    for character in file_characters_list:
        if character in dictt:
            dictt[character]+=1
        else:
            dictt[character]=1

    return dictt

def sort_list_dict(dicttt):
    listt = []
    for k in dicttt:
        if (k.isalpha()==True ):
            dict1={}
            name = 'name'
            num = 'num'
            dict1[name]= k
            dict1[num]= dicttt[k]
            listt.append(dict1)
            
    listt.sort(reverse=True, key=sort_on)   
    return listt

def return_list_listdict (llist):
    list2=[]
    for l in llist:
        dict2={}
        dict2[l['name']]= l['num']
        list2.append(dict2)
    return list2


def sort_on(dict):
    return dict["num"]