# -*- coding: utf-8 -*-


def split(s, sep=None, maxsplit=None):
    """对一个长字符串按特定子字符串进行分割

    :param s: 原长字符串
    :type s: str
    :example s: "a b c d e f"

    :param sep: 子字符串,为None时值为 " "
    :type sep: str
    :example sep: " "

    :param maxsplit: 分割次数，为None时代表全部分割
    :type maxsplit: int
    :example maxsplit: 3

    :rtype list
    :return 按特定子字符串分割后的字符
    :example ['a', 'b', 'c', 'd e f']
    """
    if sep is None:
        sep = " "

    def _split():
        if maxsplit is not None and maxsplit == 0:
            yield s
            return

        sep_length = len(sep)
        length = len(s)

        i, j = 0, 0
        split_count = 0

        while i < length:

            if s[i:i + sep_length] == sep:
                yield s[j:i]

                i += sep_length
                j = i

                split_count += 1
                if maxsplit and split_count >= maxsplit:
                    break
            else:
                i += 1
        if j <= len(s):
            yield s[j:]

    return [sub for sub in _split()]

