def convert_time(time):
    time = time.split(':')
    return int(time[0]) * 60 + int(time[1])


def solution(book_time):
    book_time.sort()
    room_list = []
    for start, end in book_time:
        start = convert_time(start)
        end = convert_time(end)

        if len(room_list) == 0:
            room_list.append([end])
        else:
            flag = False
            for room in room_list:
                if room[-1] + 10 <= start:
                    room.append(end)
                    flag = True
                    break

            if flag == False:
                room_list.append([end])

    return len(room_list)


solution([["10:00", "10:10"]])