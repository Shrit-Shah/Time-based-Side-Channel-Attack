import time

def verify_password(stored_pwd, entered_pwd):
    if len(stored_pwd) != len(entered_pwd):
        return False
    for i in range(0, len(stored_pwd)):
        if stored_pwd[i] != entered_pwd[i]:
            return False
        time.sleep(0.001) 
    return True


stored_pwd = "pass"
temp = ""
for j in range(4 , 0 , -1):
    result = {} 
    for c in "abcdefghijklmnopqrstuvwxyz":
        timed = []   
        for _ in range (1001):
            entered_pwd = temp + c + "a" * (j-1)  
            start_time = time.perf_counter()
            verify_password(stored_pwd, entered_pwd)
            end_time = time.perf_counter()
            elapsed_time = end_time - start_time
            timed.append(elapsed_time)
        timed.sort()
        median_time = timed[len(timed) // 2]
        result[c] = median_time
    max_char = max(result, key=result.get)
    temp += max_char

print("Guessed password:", temp)
    
