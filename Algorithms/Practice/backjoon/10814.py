def solution(N):
    users = []
    for _ in range(N):
        age, username = input().strip().split()
        users.append([age, username])
    users.sort(key=lambda user: user[0])
    return "\n".join([f'{user[0]} {user[1]}' for user in users])


if __name__ == "__main__":
    print(solution(int(input().strip())))
