def permutation(arr, depth, n):
    if depth == n:
        print(arr)
        return

    for i in range(depth, n):
        arr[depth], arr[i] = arr[i], arr[depth]
        permutation(arr, depth + 1, n)
        arr[depth], arr[i] = arr[i], arr[depth]

lst = [1, 2, 3]
permutation(lst, 0, len(lst))