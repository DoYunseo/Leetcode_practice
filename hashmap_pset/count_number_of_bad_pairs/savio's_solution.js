/**
 * @param {number[]} nums
 * @return {number}
 */
var countBadPairs = function (nums) {
  let badPairs = 0,
    dmap = {};

  for (let i = 0; i < nums.length; i++) {
    let value = i - nums[i];

    if (!(value in dmap)) {
      dmap[value] = 0;
    } else {
      dmap[value] += 1;
    }
    let good_count = dmap[value];
    badPairs += i - good_count;
  }
  return badPairs;
};
