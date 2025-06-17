function isIsomorphic(s, t) {
  let mapST = {},
    mapTS = {};

  for (let i = 0; i < s.length; ++i) {
    let [c1, c2] = [s[i], t[i]];

    if (
      (c1 in mapST && mapST[c1] !== c2) ||
      (c2 in mapTS && mapTS[c2] !== c1)
    ) {
      return false;
    } else {
      mapST[c1] = t[i];
      mapTS[c2] = s[i];
    }
  }
  return true;
}
