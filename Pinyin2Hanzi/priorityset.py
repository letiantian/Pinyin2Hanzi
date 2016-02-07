# coding: utf-8

import heapq

class Item(object):

    def __init__(self, score, path):
        self.__score = score
        self.__path  = path

    @property
    def score(self):
        return self.__score

    @property
    def path(self):
        return self.__path

    def __lt__(self, other):
        return self.__score < other.score

    def __le__(self, other):
        return self.__score <= other.score

    def __eq__(self, other):
        return self.__score == other.score

    def __ne__(self, other):
        return self.__score != other.score

    def __gt__(self, other):
        return self.__score > other.score

    def __ge__(self, other):
        return self.__score >= other.score

    def __str__(self):
        return '< score={0}, path={1} >'.format(self.__score, self.__path)

    def __repr__(self):
        return self.__str__()


class PrioritySet(object):

    def __init__(self, capacity):
        self.capacity = capacity
        self.data = []

    def put(self, score, path):
        assert(isinstance(path, list) == True)
        heapq.heappush(self.data, [score, Item(score, path)])
        while len(self.data) > self.capacity:
            heapq.heappop(self.data)

    def __len__(self):
        return len(self.data)

    def __iter__(self):
        for item in self.data:
            yield item[1]

    def __str__(self):
        s = '[ \n'
        for item in self.data:
            s = s + '\t' + str(item[1]) + '\n'
        s += ']'
        return s

    def __repr__(self):
        return self.__str__()
