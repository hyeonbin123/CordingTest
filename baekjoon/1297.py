import math

def calculate_tv_size(diagonal, height_ratio, width_ratio):
    ratio = math.sqrt(diagonal**2 / (height_ratio**2 + width_ratio**2))
    return math.floor(height_ratio * ratio), math.floor(width_ratio * ratio)

def main():
    D, H, W = map(int, input().split())
    height, width = calculate_tv_size(D, H, W)
    print(height, width)

if __name__ == "__main__":
    main()