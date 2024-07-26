def exercise_simulator(N, m, M, T, R):
    if m + T > M:
        return -1
    
    current_pulse = m 
    total_time = 0  
    exercise_time = 0 
    
    while exercise_time < N:
        if current_pulse + T <= M:  
            current_pulse += T
            exercise_time += 1
        else:  
            current_pulse = max(current_pulse - R, m)
        
        total_time += 1
    
    return total_time



N, m, M, T, R = map(int,input().strip().split())
print(exercise_simulator(N, m, M, T, R))