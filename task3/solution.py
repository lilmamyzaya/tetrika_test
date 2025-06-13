def appearance(intervals: dict[str, list[int]]) -> int:
    def process_intervals(intervals_list: list[int]) -> list[tuple[int, int]]:
        processed = []
        for i in range(0, len(intervals_list), 2):
            start = intervals_list[i]
            end = intervals_list[i + 1]
            if start < end:  
                processed.append((start, end))
        processed.sort()
        return processed

    def merge_intervals(intervals: list[tuple[int, int]]) -> list[tuple[int, int]]:
        if not intervals:
            return []
        
        merged = [intervals[0]]
        for current in intervals[1:]:
            last = merged[-1]
            if current[0] <= last[1]:  
                merged[-1] = (last[0], max(last[1], current[1]))
            else:
                merged.append(current)
        return merged

    lesson_start, lesson_end = intervals['lesson'][0], intervals['lesson'][1]
    
    pupil = merge_intervals(process_intervals(intervals['pupil']))
    tutor = merge_intervals(process_intervals(intervals['tutor']))

    total_time = 0
    p_idx = t_idx = 0

    while p_idx < len(pupil) and t_idx < len(tutor):
        p_start, p_end = pupil[p_idx]
        t_start, t_end = tutor[t_idx]

        intersect_start = max(p_start, t_start, lesson_start)
        intersect_end = min(p_end, t_end, lesson_end)

        if intersect_start < intersect_end:
            total_time += intersect_end - intersect_start

        if p_end < t_end:
            p_idx += 1
        else:
            t_idx += 1

    return total_time

tests = [
    {
        "intervals": {
            "lesson": [1594663200, 1594666800],
            "pupil": [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
            "tutor": [1594663290, 1594663430, 1594663443, 1594666473],
        },
        "answer": 3117,
    },
    {
        "intervals": {
            "lesson": [1594702800, 1594706400],
            "pupil": [1594702789, 1594704500, 1594702807, 1594704542, 1594704512, 1594704513, 1594704564, 1594705150, 1594704581, 1594704582, 1594704734, 1594705009, 1594705095, 1594705096, 1594705106, 1594706480, 1594705158, 1594705773, 1594705849, 1594706480, 1594706500, 1594706875, 1594706502, 1594706503, 1594706524, 1594706524, 1594706579, 1594706641],
            "tutor": [1594700035, 1594700364, 1594702749, 1594705148, 1594705149, 1594706463],
        },
        "answer": 3577,
    },
    {
        "intervals": {
            "lesson": [1594692000, 1594695600],
            "pupil": [1594692033, 1594696347],
            "tutor": [1594692017, 1594692066, 1594692068, 1594696341],
        },
        "answer": 3565,
    },
]

if __name__ == "__main__":
    for i, test in enumerate(tests):
        test_answer = appearance(test["intervals"])
        assert test_answer == test["answer"], f'Error on test case {i}, got {test_answer}, expected {test["answer"]}'
    print("All tests passed!")