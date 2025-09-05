from collections import defaultdict
from typing import List 

class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        parsed_transactions, res = [], []
        for i, t in enumerate(transactions):
            name, time, amount, city = t.split(',')
            parsed_transactions.append({
                'name': name,
                'time': int(time),
                'amount': int(amount),
                'city': city,
                'original_index': i
            })
        
        trans_list_hold_name = defaultdict(list)

        for t in parsed_transactions:
            trans_list_hold_name[t['name']].append(t)
        
        invalid = set()

        for name, trans_list in trans_list_hold_name.items():
            n = len(trans_list)
            for i in range(n):
                t1 = trans_list[i]
                
                if t1['amount'] > 1000:
                    invalid.add(t1['original_index'])
                
                for j in range(n):
                    if i != j:
                        t2 = trans_list[j]
                        if abs(t1['time'] - t2['time']) <= 60 and t1['city'] != t2['city']:
                            invalid.add(t1['original_index'])
                            invalid.add(t2['original_index'])
        for i in invalid:
            res.append(transactions[i])
        return res
                
        


