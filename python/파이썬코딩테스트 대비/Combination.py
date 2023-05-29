def combinations(arr, r):
    result = []

    def generate(index, elements):
        if len(elements) == r:
            result.append(elements[:])
            return

        if index >= len(arr):
            return

        elements.append(arr[index])
        generate(index + 1, elements)
        elements.pop()
        generate(index + 1, elements)

    generate(0, [])
    return result