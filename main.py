import sys 
from stats import get_num_words , get_character_count ,sort_list_dict ,return_list_listdict

      
def main():
    if not (len(sys.argv)==2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    path_to_book = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_book}...")
    print("----------- Word Count ----------")
    num_words = get_num_words(path_to_book)
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    character_count_dictt=get_character_count(path_to_book)
    listttt = return_list_listdict(sort_list_dict(character_count_dictt))
    for lll in listttt:
        for k in lll:
            print(f"{k}: {lll[k]}")
    print("============= END ===============")
     
main()

