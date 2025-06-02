def appearance(intervals):
    lesson_start, lesson_end = intervals["lesson"]

    def process_intervals(raw_intervals):
        intervals = []
        for i in range(0, len(raw_intervals), 2):
            start = max(raw_intervals[i], lesson_start)
            end = min(raw_intervals[i + 1], lesson_end)
            if start < end:  # only add if valid interval
                intervals.append((start, end))
        return intervals

    # get valid intervals for pupil and tutor within lesson time
    pupil = process_intervals(intervals["pupil"])
    tutor = process_intervals(intervals["tutor"])

    # find when either pupil or tutor is present
    events = []
    for start, end in pupil:
        events.append((start, 1))  # 1 = pupil enters
        events.append((end, -1))  # -1 = pupil exits
    for start, end in tutor:
        events.append((start, 2))  # 2 = tutor enters
        events.append((end, -2))  # -2 = tutor exits

    # sort all events by time
    events.sort()

    total = 0
    pupil_present = 0
    tutor_present = 0
    prev_time = None

    for time, typ in events:
        if prev_time is not None and pupil_present > 0 and tutor_present > 0:
            total += time - prev_time

        if abs(typ) == 1:
            pupil_present += typ
        else:
            tutor_present += typ

        prev_time = time

    return total


tests = [
    {
        "intervals": {
            "lesson": [1594663200, 1594666800],
            "pupil": [
                1594663340,
                1594663389,
                1594663390,
                1594663395,
                1594663396,
                1594666472,
            ],
            "tutor": [1594663290, 1594663430, 1594663443, 1594666473],
        },
        "answer": 3117,
    },
    {
        "intervals": {
            "lesson": [1594702800, 1594706400],
            "pupil": [
                1594702789,
                1594704500,
                1594702807,
                1594704542,
                1594704512,
                1594704513,
                1594704564,
                1594705150,
                1594704581,
                1594704582,
                1594704734,
                1594705009,
                1594705095,
                1594705096,
                1594705106,
                1594706480,
                1594705158,
                1594705773,
                1594705849,
                1594706480,
                1594706500,
                1594706875,
                1594706502,
                1594706503,
                1594706524,
                1594706524,
                1594706579,
                1594706641,
            ],
            "tutor": [
                1594700035,
                1594700364,
                1594702749,
                1594705148,
                1594705149,
                1594706463,
            ],
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
        assert (
            test_answer == test["answer"]
        ), f'Error on test case {i}, got {test_answer}, expected {test["answer"]}'
