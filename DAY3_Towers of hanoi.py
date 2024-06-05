class Solution:
    def moveDisks(self, N, source, destination, auxiliary, moves):
        if N == 1:
            move = "move disk {} from rod {} to rod {}".format(N, source, destination)
            moves.append(move)
            return
        self.moveDisks(N-1, source, auxiliary, destination, moves)
        move = "move disk {} from rod {} to rod {}".format(N, source, destination)
        moves.append(move)
        self.moveDisks(N-1, auxiliary, destination, source, moves)

    def toh(self, N, source, destination, auxiliary):
        moves = []  # to store the number of steps
        self.moveDisks(N, source, destination, auxiliary, moves)
        for move in moves:
            print(move)
        return len(moves)
