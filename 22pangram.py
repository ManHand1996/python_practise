
def get_missing_letter(input_str):
    full_str = "abcdefghijklmnopqrstuvwxyz"
    full_str = ''.join(map(chr, range(ord('a'), ord('z')+1)))
    input_str = input_str.strip().lower()
    
    list_1 = filter(lambda x : input_str.find(x.lower()) < 0  ,full_str) 


    
    result_str = ''.join(list_1)
    
     
    print(result_str)

get_missing_letter("")
