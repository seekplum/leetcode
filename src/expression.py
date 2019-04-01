#!/usr/bin/env python
# -*- coding:utf-8 -*-

import re
import collections

# 表达式中可能会用到的符号
NUM = r'(?P<NUM>\d+)'  # 数值
PLUS = r'(?P<PLUS>\+)'  # 加号
MINUS = r'(?P<MINUS>-)'  # 减号
TIMES = r'(?P<TIMES>\*)'  # 乘号
DIVIDE = r'(?P<DIVIDE>/)'  # 除号
LEFT_PAREN = r'(?P<LEFT_PAREN>\()'  # 左括号
RIGHT_PAREN = r'(?P<RIGHT_PAREN>\))'  # 右括号
WS = r'(?P<WS>\s+)'  # 空白字符

master_pat = re.compile('|'.join([NUM, PLUS, MINUS, TIMES,
                                  DIVIDE, LEFT_PAREN, RIGHT_PAREN, WS]))
# 令牌 类型和具体的值
Token = collections.namedtuple('Token', ['type', 'value'])


def generate_tokens(text):
    """读取表达式内容

    :param text: str 要求值的表达式
    """
    scanner = master_pat.scanner(text)
    for m in iter(scanner.match, None):
        tok = Token(m.lastgroup, m.group())
        # 忽略表达式中空白字符
        if tok.type != 'WS':
            yield tok


class ExpressionEvaluator(object):

    def __init__(self):
        self.tokens = None
        self.tok = None
        self.next_tok = None

    def parse(self, text):
        self.tokens = generate_tokens(text)
        self.tok = None  # Last symbol consumed
        self.next_tok = None  # Next symbol token
        self._advance()  # Load first lookahead token
        return self.expr()

    def _advance(self):
        """提取下个令牌
        """
        self.tok, self.next_tok = self.next_tok, next(self.tokens, None)

    def _accept(self, tok_type):
        """测试下一个令牌, 如果正常，则再提取下个令牌


        :rtype bool
        """
        if self.next_tok and self.next_tok.type == tok_type:
            self._advance()
            return True
        else:
            return False

    def _expect(self, tok_type):
        """检查下个令牌类型是否正常
                正常：
                    继续提取下一个令牌
                不正常：
                    抛出语法错误
        :param tok_type: str 令牌类型
        """
        if not self._accept(tok_type):
            raise SyntaxError('Expected ' + tok_type)

    def expr(self):
        """计算 加法和减法

        :rtype int, float
        """
        expr_val = self.term()
        while self._accept('PLUS') or self._accept('MINUS'):
            op = self.tok.type
            right = self.term()
            if op == 'PLUS':
                expr_val += right
            elif op == 'MINUS':
                expr_val -= right
        return expr_val

    def term(self):
        """计算 除法和乘法

        :rtype int, float
        """
        term_val = self.factor()
        while self._accept('TIMES') or self._accept('DIVIDE'):
            op = self.tok.type
            right = self.factor()
            if op == 'TIMES':
                term_val *= right
            elif op == 'DIVIDE':
                term_val /= right
        return term_val

    def factor(self):
        """计算括号中的值

        :rtype int, float
        """
        if self._accept('NUM'):
            return int(self.tok.value)
        elif self._accept('LEFT_PAREN'):
            expr_val = self.expr()
            self._expect('RIGHT_PAREN')
            return expr_val
        else:
            raise SyntaxError('Expected NUMBER or LEFT PAREN')


def descent_parser():
    e = ExpressionEvaluator()
    print(e.parse('2 + (3 + 4 * 5) * 6'))


if __name__ == '__main__':
    descent_parser()
