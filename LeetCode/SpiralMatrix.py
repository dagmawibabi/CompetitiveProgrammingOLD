from ast import MatchOr
from re import L


def spiralOrder(matrix):
    first = [];
    links = [];
    lastReverse = [];
    middle = [];
    final = [];
    if len(matrix) > 1:
        # get first
        for i in range(0, len(matrix[0]) - 1):
            first.append(matrix[0][i]);
        # get link
        for i in matrix:
            links.append(i[len(i)- 1]);
        # get last reversed
        lastReverse = (matrix[len(matrix) - 1]);
        lastReverse.pop();
        lastReverse.reverse();
        # get middle
        for i in range(1, len(matrix) -1):
            matrix[i].pop();
            for i in matrix[i]:
                middle.append(i);
        # finalize
        for i in first:
            final.append(i);
        for i in links:
            final.append(i);
        for i in lastReverse:
            final.append(i);
        for i in middle:
            final.append(i);
    else:
        final = matrix[0];
    # Result
    return final;
# spiralOrder([[1,2,3],[4,5,6],[7,8,9]]);
spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]);