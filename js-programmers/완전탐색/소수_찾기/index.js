// [important]

function solution(numbers) {
  const primeSet = new Set();
  comb(numbers.split(""), "");
  /**
   *
   * @param {number[]} restNums
   * @param {string} curr
   */
  function comb(restNums, curr) {
    const currNum = Number.parseInt(curr);
    if (!Number.isNaN(currNum) && !primeSet.has(currNum)) {
      if (isPrime(currNum)) {
        primeSet.add(currNum);
      }
    }
    if (restNums.length > 0) {
      restNums.forEach((num, idx) => {
        const newRestNums = [...restNums];
        newRestNums.splice(idx, 1);
        comb(newRestNums, curr + num);
      });
    }
  }

  /**
   *
   * @param {number} num
   * @returns {boolean}
   */
  function isPrime(num) {
    if (num < 2) return false;
    for (let i = 2; i <= Math.sqrt(num); i++) {
      if (num % i === 0) {
        return false;
      }
    }
    return true;
  }

  return primeSet.size;
}

// console.log(solution("17"));
