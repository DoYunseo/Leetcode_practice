from typing import List


class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort(key=lambda x: x[0])
        merged_meetings = [meetings[0]]

        for i in range(1, len(meetings)):
            start_time = meetings[i][0]
            end_time = meetings[i][1]
            if start_time <= merged_meetings[-1][1]:
                merged_meetings[-1][0] = min(merged_meetings[-1][0], start_time)
                merged_meetings[-1][1] = max(merged_meetings[-1][1], end_time)
            else:
                merged_meetings.append(meetings[i])

        total_meeting_days = 0

        for start, end in merged_meetings:
            total_meeting_days += end - start + 1

        return days - total_meeting_days
