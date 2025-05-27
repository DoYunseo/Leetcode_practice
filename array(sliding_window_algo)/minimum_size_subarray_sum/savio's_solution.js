/**
 * @param {number} target
 * @param {number[]} nums
 * @return {number}
 */
var minSubArrayLen = function(target, nums) {
    let start = 0,
        end = 0,
        r_sum = 0,
        mini = Infinity
        n = nums.length

        while (end  < n) {
            r_sum += nums[end]

            while (r_sum >= target) {
                mini = Math.min(mini, end - start + 1)
                r_sum -= nums[start]
                start += 1
            }

            end += 1
        }
    if (mini == Infinity) {
        return 0
    }
    else {
        return mini
    }

};