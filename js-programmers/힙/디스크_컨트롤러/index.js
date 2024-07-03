function solution(input) {
  const totalLength = input.length;
  const jobs = input
    .map((job) => ({ time: job[0], taken: job[1] }))
    .sort((a, b) => b.time - a.time);
  const heap = [];
  let time = -1;
  let totalTaken = 0;
  let currTask = null;
  while (true) {
    time += 1;
    if (currTask) {
      currTask.taken -= 1;
      if (currTask.taken > 0) {
        continue;
      }
      totalTaken += time - currTask.time;
    }
    if (jobs.length <= 0 && heap.length <= 0) {
      break;
    }
    while (jobs.length > 0 && jobs[jobs.length - 1].time <= time) {
      heap.push(jobs.pop());
    }
    heap.sort((a, b) => b.taken - a.taken);
    currTask = heap.pop();
  }

  return Math.floor(totalTaken / totalLength);
}

function solution(input) {
  const totalLength = input.length;
  const jobs = input
    .map((job) => ({ time: job[0], taken: job[1] }))
    .sort((a, b) => b.time - a.time || b.taken - a.taken);
  const heap = [];
  let time = 0;
  let totalTaken = 0;
  while (jobs.length > 0 || heap.length > 0) {
    while (jobs.length > 0 && jobs[jobs.length - 1].time <= time) {
      heap.push(jobs.pop());
    }
    heap.sort((a, b) => b.taken - a.taken || b.time - a.time);
    let currTask = null;
    if (heap.length > 0) {
      currTask = heap.pop();
    } else {
      currTask = jobs.pop();
      time = currTask.time;
    }
    time += currTask.taken;
    totalTaken += time - currTask.time;
  }

  return Math.floor(totalTaken / totalLength);
}

console.log(
  solution([
    [0, 3],
    [1, 9],
    [2, 6],
  ])
);

console.log(
  solution([
    [1, 4],
    [7, 9],
    [1000, 3],
  ])
);
