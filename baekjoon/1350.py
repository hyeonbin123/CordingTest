from math import ceil
def calculate_disk_space(file_sizes, cluster_size):
    total_space=0
    for size in file_sizes:
        if size == 0: continue
        total_space += ceil(size/cluster_size)*cluster_size
    return total_space

def main():
    N = int(input().strip())
    file_sizes = list(map(int, input().strip().split()))
    cluster_size = int(input().strip())
    print(calculate_disk_space(file_sizes, cluster_size))

if __name__ == "__main__":
    main()