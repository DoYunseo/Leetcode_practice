/**
 * @param {number[]} arr
 * @return {boolean}
 */
var threeConsecutiveOdds = function (arr) {
  if (arr.length < 3) return false;
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] % 2 == 1 && arr[i + 1] % 2 == 1 && arr[i + 2] % 2 == 1) {
      return true;
    }
  }
  return false;
};
