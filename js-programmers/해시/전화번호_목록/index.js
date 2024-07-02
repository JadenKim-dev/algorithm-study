function solution(phone_book) {
  phone_book.sort((a, b) => a.length - b.length);
  let currLength = 0;
  const data = {};
  for (const number of phone_book) {
    for (let i = 1; i <= currLength; i++) {
      const prefix = number.substring(0, i);
      if (data[prefix]) return false;
    }
    data[number] = true;
    currLength = number.length;
  }
  return true;
}

function solution(phone_book) {
  phone_book.sort();
  console.log(phone_book);
  return !phone_book.some((_, idx) => {
    if (idx >= phone_book.length - 1) return false;
    return phone_book[idx + 1].startsWith(phone_book[idx]);
  });
}

console.log(solution(["119", "97674223", "1195524421"]));
