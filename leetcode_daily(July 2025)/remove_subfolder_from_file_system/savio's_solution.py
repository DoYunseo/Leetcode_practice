class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        result = []

        for sub in folder:
            if not result or not sub.startswith(result[-1] + '/'): 
                result.append(sub)
        return result
    
        