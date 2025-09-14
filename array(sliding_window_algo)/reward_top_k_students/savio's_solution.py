from typing import List
import heapq


class Solution:
    def topStudents(
        self,
        positive_feedback: List[str],
        negative_feedback: List[str],
        report: List[str],
        student_id: List[int],
        k: int,
    ) -> List[int]:
        student_points = {}
        negative_set = set(negative_feedback)
        positive_set = set(positive_feedback)

        for idx, sentence in enumerate(report):
            student_points[student_id[idx]] = 0
            constructed_sentence = [word for word in sentence.split(" ")]
            for word in constructed_sentence:
                if word in negative_set:
                    student_points[student_id[idx]] -= 1
                elif word in positive_set:
                    student_points[student_id[idx]] += 3
        hp = []
        result = []
        print(student_points)
        for key, val in student_points.items():
            doc = (-val, key)
            heapq.heappush(hp, doc)
        for i in range(k):
            _, id = heapq.heappop(hp)
            result.append(id)
        return result
