def partial_sums(*res):
    result = [0]
    for i in res:
        list_sums = result[-1]
        result.append(list_sums + i)
    return result


print(partial_sums(13))
print(partial_sums(1, 0.5, 0.25, 0.125))