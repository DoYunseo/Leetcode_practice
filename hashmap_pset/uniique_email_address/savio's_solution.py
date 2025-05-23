from typing import List
from collections import defaultdict
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        countUnique = defaultdict(int) 
        for email in emails:
            local, domain = email.split("@")
            construct_email = ""
            for char in local:
                if char == ".":
                    continue
                elif char == "+":
                    break
                else:
                    construct_email += char
            construct_email += "@" + domain
            countUnique[construct_email] += 1
        return len(countUnique)

