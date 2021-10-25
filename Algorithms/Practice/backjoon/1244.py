if __name__ == "__main__":
    number_of_switches = int(input().strip())
    switches = [0] + list(map(int, input().split()))

    number_of_students = int(input().strip())
    for _ in range(number_of_students):
        op, switch = map(int, input().split())

        idx = switch
        switches[idx] = not switches[idx]

        if op == 1:
            # 남학생
            while 1 < idx + switch < len(switches):
                idx += switch
                switches[idx] = not switches[idx]

        elif op == 2:
            # 여학생
            step = 1
            while 0 < idx - step and idx + step < len(switches):
                if int(switches[idx - step]) != int(switches[idx + step]):
                    break
                switches[idx - step] = not switches[idx - step]
                switches[idx + step] = not switches[idx + step]

                step += 1

    switches = switches[1:]
    while switches:
        print(" ".join(map(lambda switch: str(int(switch)), switches[:20])), end="\n")
        switches = switches[20:]
