function oddSum(min, max) {
  let total = 0;
  for (let i = min; i <= max; i++) {
    if (i % 2 !== 0) {
      total += i;
    }
  }
  return total;
}
