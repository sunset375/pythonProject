# Even Subarray practice Question
# help:  https://www.geeksforgeeks.org/number-subarrays-m-odd-numbers/
# github test
def evenSubarray(numbers, k):
    count = 0
    n = len(numbers)
    for i in range(n):
        temp2 = []
        p = 0
        check = set()
        for j in range(i, n):
            if i == 0:
                if numbers[j] % 2 == 1:
                    temp2.append(1)
                else:
                    temp2.append(0)
                if temp2[p] <= k and numbers[j] not in check:
                    count += 1
                    check.add(numbers[j])
            else:
                if numbers[j] % 2 == 1:
                    temp2.append(temp1[p] + 1)
                else:
                    temp2.append(temp1[p])
                if temp2[p] <= k and tuple(numbers[k:j + 1]) not in check:
                    count += 1
                    check.add(tuple(numbers[p:j + 1]))
            p += 1
        temp1 = list(temp2)

    return count


if __name__ == "__main__":
    numbers = [6, 3, 5, 8]

    k = 1
    print(evenSubarray(numbers, k))