#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    sums = []

    for i in range(0, length):
        sum_minus = limit - weights[i]
        if hash_table_retrieve(ht, weights[i]) is None:
            hash_table_insert(ht, sum_minus, i)
        else:
            if hash_table_retrieve(ht, weights[i]) <= i:
                sums.append(i)
                sums.append(hash_table_retrieve(ht, weights[i]))
            else:
                sums.append(hash_table_retrieve(ht, weights[i]))
                sums.append(i)

    if len(sums) is 0:
        return None
    else:
        return sums


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")


weights_3 = [4, 6, 10, 15, 16]
answer_3 = get_indices_of_item_weights(weights_3, 5, 21)
