import hashlib
from pickle import NONE

file_path = '/home/manhand/Downloads/Python-3.9.10.tar.xz'
def get_data():
    data = b''
    with open(file_path,'rb') as f:
        # while f.readable():
        d = f.read(2048)
        data += d
        yield data

def test_yield():
    

def get_hashcode():
    digester = hashlib.md5()
    # with open(file_path,'rb') as f:
    #     fiter = iter(lambda:f.read(2048), b'')
    #     for data in fiter:
    #         digester.update(data)
    
    f = get_data()
    data = b''
    for d in f:
        data = d
    digester.update(data)
    return digester.hexdigest()




if __name__ == '__main__':
    print(get_hashcode())


