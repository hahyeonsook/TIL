# python3 시간초과
def solution(N):
    sequence = list(map(int, input().split()))[::-1]
    operators = list(map(int, input().split()))

    def choice(numbers, ops, choiced, results):
        if len(numbers) == 1:
            results.append(numbers[-1])
            return results, numbers

        op1 = numbers.pop()
        for idx, op in enumerate(ops):
            if choiced[idx]:
                continue

            choiced[idx] = True
            op2 = numbers.pop()
            if op == "+":
                result = op1 + op2
            elif op == "-":
                result = op1 - op2
            elif op == "*":
                result = op1 * op2
            elif op == "/":
                if op1 < 0:
                    result = -((-op1) // op2)
                else:
                    result = op1 // op2

            results, _ = choice(numbers + [result], ops, choiced, results)

            choiced[idx] = False
            numbers.append(op2)
        numbers.append(op1)
        return results, numbers

    results, _ = choice(sequence, operators, [False] * len(operators), [])
    return f"{max(results)}\n{min(results)}"


if __name__ == "__main__":
    print(solution(int(input().strip())))
