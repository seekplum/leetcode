#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
#=============================================================================
#  ProjectName: seekplum
#     FileName: hash_storage
#         Desc: 普通hash算法
#       Author: seekplum
#        Email: 1131909224m@sina.cn
#     HomePage: seekplum.github.io
#       Create: 2018-05-27 21:04
#=============================================================================
"""

from bisect import bisect_left
from hashlib import md5
from struct import unpack_from

ITEMS = 10000000  # 所有值数量
NODES = 100  # 节点数量1
NODES2 = 101  # 节点数量2
VALUES = 1000  # 虚拟节点数量


def _hash(value):
    """计算哈希值

    :param value 被计算的值
    :type value str

    :rtype int
    :return 哈希值
    """
    k = md5(value).digest()
    return unpack_from(">I", k)[0]


def normal_hash():
    """普通hash算法
    """
    change = 0
    node_stat = [i for i in xrange(NODES)]
    for item in xrange(ITEMS):
        # 主要依赖的md5算法能够比较均匀的分布
        h = _hash(str(item))
        n = h % NODES
        node_stat[n] += 1
        if h % NODES2 != n:
            change += 1

    _ave = ITEMS / NODES
    _max = max(node_stat)
    _min = min(node_stat)

    print "Ave: {}".format(_ave)
    print "Max: {}, {:.2f}%".format(_max, (_max - _ave) * 100.0 / _ave)
    print "Min: {}, {:.2f}%".format(_min, (_ave - _min) * 100.0 / _ave)
    print "Change: {}, {:.2f}%".format(change, change * 100.0 / ITEMS)


def consistency_hash1():
    """一致性hash算法

    一致性哈希是一种特殊的哈希算法，在使用一致性哈希算法后，哈希表槽位数(大小)的改变平均值需要对 K / N个关键字进行重新映射，其中K是关键字的数量，
    n是槽位数量，在传统的哈希表中，添加或删除一个槽位的几乎要对所有的关键字进行重新映射

    主要解决的问题在于当node节点数量发生变化是，如何保证尽量少的迁移
    当增加或删除节点是时，对于大多数item，保证原来分配到的某个node，现在依然应该分配到那个node，将数据迁移量降到最低

    会带来的问题，节点在hash后，在环上的分布不均匀，导致每个节点实际占据环上的区间大小不一致
    """
    ring = [_hash(str(n)) for n in range(NODES)]
    ring2 = [_hash(str(n)) for n in range(NODES2)]
    ring.sort()
    ring2.sort()

    change = 0
    node_stat = [i for i in xrange(NODES)]
    for item in xrange(ITEMS):
        h = _hash(str(item))
        n = bisect_left(ring, h) % NODES
        n2 = bisect_left(ring2, h) % NODES2
        node_stat[n] += 1
        if n2 != n:
            change += 1

    _ave = ITEMS / NODES
    _max = max(node_stat)
    _min = min(node_stat)

    print "Ave: {}".format(_ave)
    print "Max: {}, {:.2f}%".format(_max, (_max - _ave) * 100.0 / _ave)
    print "Min: {}, {:.2f}%".format(_min, (_ave - _min) * 100.0 / _ave)
    print "Change: {}, {:.2f}%".format(change, change * 100.0 / ITEMS)


def consistency_hash2():
    """优化后的一致性hash算法

    增加虚拟节点，使得每个节点在环上的区间更均匀，这样就保证了在节点变换是，尽可能小的影响数据分布的变换，同时又保证了数据分布的均匀
    """
    ring = []
    # 增加虚拟节点，是每个节点的分布更均匀
    hash2node = {}
    for n in xrange(NODES):
        for v in range(VALUES):
            h = _hash(str(n) + str(v))
            ring.append(h)
            hash2node[h] = n
    ring.sort()
    ring2 = []
    for n in xrange(NODES2):
        for v in range(VALUES):
            h = _hash(str(n) + str(v))
            ring2.append(h)
            hash2node[h] = n
    ring2.sort()

    change = 0

    node_stat = [i for i in xrange(NODES)]
    for item in xrange(ITEMS):
        h = _hash(str(item))
        n = bisect_left(ring, h) % (NODES2 * VALUES)
        node_stat[hash2node[ring[n]]] += 1
        n2 = bisect_left(ring2, h) % (NODES2 * VALUES)
        if hash2node[ring[n]] != hash2node[ring2[n2]]:
            change += 1

    _ave = ITEMS / NODES
    _max = max(node_stat)
    _min = min(node_stat)

    print "Ave: {}".format(_ave)
    print "Max: {}, {:.2f}%".format(_max, (_max - _ave) * 100.0 / _ave)
    print "Min: {}, {:.2f}%".format(_min, (_ave - _min) * 100.0 / _ave)
    print "Change: {}, {:.2f}%".format(change, change * 100.0 / ITEMS)


def main():
    normal_hash()
    consistency_hash1()
    consistency_hash2()


if __name__ == '__main__':
    main()
