// 7-has_array_values.js
function hasValuesFromArray(set, arr) {
  for (const value of arr) {
    if (!set.has(value)) {
      return false;
    }
  }
  return true;
}

export default hasValuesFromArray;
