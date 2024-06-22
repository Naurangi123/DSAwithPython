def hash_insert(T, k):
    m = len(T) 
    i = 0  

    while True:
        j = hash(k) % m  
        if T[j] == 0:  
            T[j] = k  
            return k  
        else:
            i += 1 
            if i == m: 
                return None  

T = [1, 2, 3, 4, 5, 6] 
print(hash_insert(T, 4))  
