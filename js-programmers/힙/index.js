// 최댓값과 최솟값을 구할 때 heap sort 알고리즘을 사용하면 쉽게 해결
const heap = [];

function swap(num) {
  if (heap.length === 0) heap.push(num);
  else {
    let flag = false;
    let i = 0;
    while (!flag) {
      if (num < heap[i]) i++;
      else {
        heap.splice(i, 0, num);
        flag = true;
      }
    }
  }
}

function heapInsert(num) {
  if (heap.length === 0) {
    heap.push(num);
    return;
  }
  let idx = 0;
  while (true) {
    if (heap[idx] > num) {
      idx += 1;
    } else {
      heap.splice(idx, 0, num);
      return;
    }
  }
}
