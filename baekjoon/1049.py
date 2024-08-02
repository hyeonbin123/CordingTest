def min_cost_for_guitar_strings(n, brands):
    min_package = min(brands, key=lambda x: x[0])[0]
    min_single = min(brands, key=lambda x: x[1])[1]
    
    package_count = (n + 5) // 6
    package_cost = package_count * min_package
    
    combined_cost = (n // 6) * min_package + (n % 6) * min_single
    
    single_cost = n * min_single
    
    return min(package_cost, combined_cost, single_cost)

n, m = map(int, input().split())
brands = [tuple(map(int, input().split())) for _ in range(m)]

print(min_cost_for_guitar_strings(n, brands))