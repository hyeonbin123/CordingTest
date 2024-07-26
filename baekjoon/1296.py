def calculate_probability(name, team_name):
    combined = name + team_name
    L = combined.count('L')
    O = combined.count('O')
    V = combined.count('V')
    E = combined.count('E')
    
    return ((L+O) * (L+V) * (L+E) * (O+V) * (O+E) * (V+E)) % 100

def find_best_team_name(name, team_names):
    best_prob = -1
    best_team = ''
    
    for team in team_names:
        prob = calculate_probability(name, team)
        if prob > best_prob or (prob == best_prob and team < best_team):
            best_prob = prob
            best_team = team
    
    return best_team

def main():
    name = input().strip()
    n = int(input().strip())
    team_names = [input().strip() for _ in range(n)]
    
    best_team = find_best_team_name(name, team_names)
    print(best_team)

if __name__ == "__main__":
    main()