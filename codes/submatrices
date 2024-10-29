class Solution:
    def is_square(self, matrix: List[List[int]], i_start:int, j_start:int, size: int):
        """validates if valid square"""
        for i in range(i_start, i_start+size):
            for j in range(j_start, j_start+size):
                if not matrix[i][j]:
                    return False
        return True
    
    def count_squares(self, matrix: List[List[int]]) -> int:
        count = 0
        size = 1
        """check if square is possible without iteratively creating a DP matrix"""
        while size <= len(matrix) and size <= len(matrix[0]):
            for i in range(0, len(matrix)-size+1):
                for j in range(0, len(matrix[0])-size+1):
                    if matrix[i][j] and self.isSquare(matrix, i, j, size):
                        count += 1
            size += 1
        return count
