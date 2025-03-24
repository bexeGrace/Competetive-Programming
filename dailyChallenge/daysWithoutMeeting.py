from typing import List

class Solution:
    def countDaysWithoutMeetings(self, days: int, meetings: List[List[int]]) -> int:
        if not meetings:
            return days
        
        meetings.sort()

        merged_meetings = []
        start, end = meetings[0]

        for s, e in meetings[1:]:
            if s <= end:
                end = max(end, e)
            else:
                merged_meetings.append((start, end))
                start, end = s, e
        merged_meetings.append((start, end))

        meeting_days = sum(e - s + 1 for s, e in merged_meetings)

        return days - meeting_days
print(Solution().countDaysWithoutMeetings(57, [[3,49],[23,44],[21,56],[26,55],[23,52],[2,9],[1,48],[3,31]])) # 1
        