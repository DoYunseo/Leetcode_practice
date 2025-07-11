def min_window(str1, str2):
    size_str1, size_str2 = len(str1), len(str2)

    min_sub_len = float('inf')
    index_s1, index_s2 = 0, 0
    min_subsequence = ""

    while index_s1 < size_str1:
        if str1[index_s1] == str2[index_s2]:
            if index_s2 == 0:
                start = index_s1 
            if index_s2 == size_str2:
                end = index_
            
                if end - start + 1 < min_sub_len:
                    min_sub_len = end - start + 1
                    min_subsequence = str1[start : end + 1]
                index_s1 = start
                index_s2 = 0
        index_s1 += 1

    return min_subsequence