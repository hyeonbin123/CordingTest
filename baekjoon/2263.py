import sys
input = sys.stdin.readline
def find_preorder(n, inorder, postorder):
    if not inorder:
        return []

    position = {val: idx for idx, val in enumerate(inorder)}
    preorder = []
    stack = [(0, n - 1, 0, n - 1)]

    while stack:
        in_start, in_end, post_start, post_end = stack.pop()

        if in_start > in_end or post_start > post_end:
            continue

        root = postorder[post_end]
        preorder.append(root)

        root_idx = position[root]
        left_size = root_idx - in_start

        # 오른쪽 서브트리를 먼저 스택에 추가 (나중에 처리됨)
        if root_idx + 1 <= in_end:
            stack.append((root_idx + 1, in_end, post_start + left_size, post_end - 1))

        # 왼쪽 서브트리를 스택에 추가
        if in_start <= root_idx - 1:
            stack.append((in_start, root_idx - 1, post_start, post_start + left_size - 1))

    return preorder

# 입력 받기
n = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))

# 프리오더 찾기
preorder = find_preorder(n, inorder, postorder)

# 결과 출력
print(*preorder)