def solution(L, C):
    chars = sorted(input().split())
    visited = [False] * C
    vowel = set(["a", "e", "i", "o", "u"])

    def dfs(sidx, cipher, ciphers):
        if len(cipher) == L:
            if 1 < len(set(cipher) - vowel) < len(cipher):
                ciphers.append(cipher)
            return cipher, ciphers

        for idx in range(sidx, C):
            if not visited[idx]:
                visited[idx] = True
                _, ciphers = dfs(idx + 1, cipher + chars[idx], ciphers)
                visited[idx] = False
        return cipher, ciphers

    _, ciphers = dfs(0, "", [])
    return "\n".join(ciphers)


if __name__ == "__main__":
    print(solution(*map(int, input().split())))
