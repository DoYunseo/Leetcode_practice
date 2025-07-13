from typing import List

class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        m_copy = trainers[:]
        players.sort()
        m_copy.sort()

        if players == m_copy:
            return len(players)

        trainers.sort(reverse=True)

        f_trainer = 0
        max_count = 0

        for player in players:
            if f_trainer < len(trainers) and player <= trainers[f_trainer]:
                max_count += 1
            f_trainer += 1
        return max_count


        