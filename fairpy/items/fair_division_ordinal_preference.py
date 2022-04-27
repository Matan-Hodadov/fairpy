"""
Fair Division under Ordinal Preferences:
Computing Envy-Free Allocations of Indivisible Goods

Sylvain Bouveret, Ulle Endriss and Jer´ ome Lang

2010

link:
https://books.google.co.il/books?hl=iw&lr=&id=cLqiEJVT3u8C&oi=fnd&pg=PA387&dq=Fair+Division+under+Ordinal+Preferences:+Computing+Envy-Free+Allocations+of+Indivisible+Goods&ots=GrWpDNui8t&sig=1VzhbXQpPSzGQbuGAC9Gf4S2tWI&redir_esc=y#v=onepage&q=Fair%20Division%20under%20Ordinal%20Preferences%3A%20Computing%20Envy-Free%20Allocations%20of%20Indivisible%20Goods&f=false

In this article there are 1 main algorithm (getPPE_PEF) and 6 more secondary
Which means a total of 7 algorithms
"""

from typing import *


# possible envy-free
def isPEF(m: int, n: int, preference: dict, allocation: dict) -> bool:
    """
    :param m: int
    :param n: int
    :param preference: dict
    :param allocation: dict
    :return: if allocation is PEF true, else false

    check if NEF is PEF
    >>> isNEF(5, 2, {1: "abcd", 2: "dcba"}, {1: "ab", 2: "dc"})
    True

    >>> isPEF(5, 2, {1: "abcd", 2: "dcba"}, {1: "ad", 2: "bc"})
    True

    >>> isPEF(3, 2, {1: "abc", 2: "abc"}, {1: "b", 2: "ac"})
    True
    """
    return None


# necessarily envy-free
def isNEF(m: int, n: int, preference: dict, allocation: dict) -> bool:
    """
    :param m: int
    :param n: int
    :param preference: dict
    :param allocation: dict
    :return: if allocation is NEF true, else false

    check if NEF is not NEF
    >>> isNEF(5, 2, {1: "abcd", 2: "dcba"}, {1: "ad", 2: "bc"})
    False

    >>> isNEF(5, 2, {1: "abcd", 2: "dcba"}, {1: "ab", 2: "dc"})
    True

    >>> isNEF(3, 2, {1: "cba", 2: "abc"}, {1: "c", 2: "ab"})
    True
    """
    return None


# possibly Pareto-dominates
def isPPD(preference: dict, alloc1: dict, alloc2: dict) -> bool:
    """
    :param preference:
    :param alloc1:
    :param alloc2:
    :return: if alloc1 is PPD on alloc2 return true, else false

    check if NPD is PPD
    >>> isPPD({1: "abcdef", 2: "fedcba"}, {1: "abc", 2: "def"}, {1: "ace", 2: "bdf"})
    return True

    >>> isPPD({1: "abcdef", 2: "fedcba"}, {1: "adf", 2: "bce"}, {1: "ace", 2: "bdf"})
    return True

    check alloc on the same alloc
    >>> isPPD({1: "abcdef", 2: "fedcba"}, {1: "adf", 2: "bce"}, {1: "adf", 2: "bce"})
    return False
    """
    return None


# necessarily Pareto dominates
def isNPD(preference: dict, alloc1: dict, alloc2: dict) -> bool:
    """
    :param preference:
    :param alloc1:
    :param alloc2:
    :return: if alloc1 is NPD on alloc2 return true, else false

    >>> isNPD({1: "abcdef", 2: "fedcba"}, {1: "abc", 2: "def"}, {1: "ace", 2: "bdf"})
    return True

    check alloc on the same alloc
    >>> isNPD({1: "abcdef", 2: "fedcba"}, {1: "ace", 2: "bdf"}, {1: "ace", 2: "bdf"})
    return False
    """
    return None


# possibly pareto efficient
def isPPE(preference: dict, alloc: dict) -> bool:
    """
    :param preference:
    :param alloc:
    :return: if alloc is PPE return true, else false

    >>> isPPE({1: "abc", 2: "abc", 3: "cba"}, {1: "b", 2: "a", 3: "c"})
    return True
    """
    return None


# necessarily pareto efficient
def isNPE(preference: dict, alloc: dict) -> bool:
    """
    :param preference:
    :param alloc:
    :return: if alloc is NPE return true, else false

    >>> isNPE({1: "abc", 2: "bac", 3: "cba"}, {1: "a", 2: "b", 3: "c"})
    return True

    check alloc on the same alloc
    >>> isNPE({1: "abcdef", 2: "fedcba"}, {1: "ace", 2: "bdf"})
    return False
    """
    return None


# get PPE PEF alloc
def getPPE_PEF(m: int, n: int, preference: dict) -> dict:
    """
    :param m: 
    :param n: 
    :param preference: 
    :return: return a PPE PEF allocation if there is one. else return None
    
    >>> getPPE_PEF(6, 4, {1: "abcdef", 2: "adbcef", 3: "bacdfe", 4: "bacefd"})
    {1: "a", 2: "df", 3: "b", 4: "ce"}

    whem m smaller then 2n-k
    >>> getPPE_PEF(6, 4, {1: "abcdef", 2: "adbcef", 3: "bacdfe", 4: "efabdc"})
    None
    """
    return None




