function solution(triangle) {
  for (let i = 0; i < triangle.length - 1; i++) {
      const fromCol = triangle[i];
      const toCol = [...triangle[i+1]];
      for (let j = 0; j < fromCol.length; j++) {
          triangle[i+1][j] = Math.max(triangle[i+1][j], toCol[j] + fromCol[j]);
          triangle[i+1][j+1] = Math.max(triangle[i+1][j+1], toCol[j+1] + fromCol[j]);
      }
  }
  return Math.max(...triangle[triangle.length - 1]);
}