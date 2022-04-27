from fairDivision import *
import pytest


class TestFairDivision:
    def test_isPEF(self):
        assert isPEF(5, 2, {1: "abcd", 2: "dcba"}, {1: "ad", 2: "bc"})
        assert isPEF(3, 2, {1: "abc", 2: "abc"}, {1: "b", 2: "ac"})
        with pytest.raises(TypeError):
            isPEF(-1, 2, {1: "abcd", 2: "dcba"}, {1: "ad", 2: "bc"})
            isPEF(5, -1, {1: "abcd", 2: "dcba"}, {1: "ad", 2: "bc"})
            isPEF(5, 2, {}, {1: "ad", 2: "bc"})
            isPEF(5, 2, {1: "abcd", 2: "dcba"}, {1: "ad", 4: "bc"})
            isPEF(5, 2, {1: "abcd", 2: "dcba"}, {3: "ad", 2: "bc"})

    def test_isNEF(self):
        assert isNEF(5, 2, {1: "abcd", 2: "dcba"}, {1: "ab", 2: "dc"})
        assert isNEF(5, 2, {1: "abcd", 2: "dcba"}, {1: "ad", 2: "bc"}) is False
        assert isNEF(3, 2, {1: "cba", 2: "abc"}, {1: "c", 2: "ab"})
        assert isNEF(3, 2, {1: "abc", 2: "abc"}, {1: "b", 2: "ac"}) is False
        with pytest.raises(TypeError):
            isNEF(-1, 2, {1: "abcd", 2: "dcba"}, {1: "ad", 2: "bc"})
            isNEF(5, -1, {1: "abcd", 2: "dcba"}, {1: "ad", 2: "bc"})
            isNEF(5, 2, {}, {1: "ad", 2: "bc"})
            isNEF(5, 2, {1: "abcd", 2: "dcba"}, {1: "ad", 4: "bc"})
            isNEF(5, 2, {1: "abcd", 2: "dcba"}, {3: "ad", 2: "bc"})

    def test_isPPD(self):
        assert isPPD({1: "abcdef", 2: "fedcba"}, {1: "abc", 2: "def"}, {1: "ace", 2: "bdf"})
        assert isPPD({1: "abcdef", 2: "fedcba"}, {1: "adf", 2: "bce"}, {1: "ace", 2: "bdf"})
        assert isPPD({1: "abcdef", 2: "fedcba"}, {1: "adf", 2: "bce"}, {1: "adf", 2: "bce"}) is False
        assert isPPD({1: "abcdef", 2: "fedcba"}, {1: "abc", 2: "def"}, {1: "ace", 2: "bdf"}) is False
        with pytest.raises(TypeError):
            isPPD({}, {1: "abcd", 2: "dcba"}, {1: "ad", 2: "bc"})
            isPPD({1: "abcd", 2: "dcba"}, {}, {})
            isPPD({}, {}, {1: "ad", 2: "bc"})
            isPPD({1: "abcd", 2: "dcba"}, {1: "ad", 2: "bc"}, {3: "ad", 2: "bc"})

    def test_isNPD(self):
        assert isNPD({1: "abcdef", 2: "fedcba"}, {1: "abc", 2: "def"}, {1: "ace", 2: "bdf"})
        assert isNPD({1: "abcdef", 2: "fedcba"}, {1: "adf", 2: "bce"}, {1: "ace", 2: "bdf"}) is False
        assert isNPD({1: "abcdef", 2: "fedcba"}, {1: "ace", 2: "bdf"}, {1: "ace", 2: "bdf"}) is False
        with pytest.raises(TypeError):
            isNPD({}, {1: "abcd", 2: "dcba"}, {1: "ad", 2: "bc"})
            isNPD({1: "abcd", 2: "dcba"}, {}, {})
            isNPD({}, {}, {1: "ad", 2: "bc"})
            isNPD({1: "abcd", 2: "dcba"}, {1: "ad", 2: "bc"}, {3: "ad", 2: "bc"})

    def test_isPPE(self):
        assert isPPE({1: "abc", 2: "abc", 3: "cba"}, {1: "b", 2: "a", 3: "c"})
        assert isPPE({1: "abc", 2: "abc", 3: "cba"}, {}) is False
        with pytest.raises(TypeError):
            isPPE({}, {1: "abcd", 2: "dcba"})
            isPPE({1: "abcd", 2: "dcba"})
            isPPE({1: "ad", 2: "bc", 3: ""}, {1: "b", 2: "a", 3: "c"})

    def test_isNPE(self):
        assert isNPE({1: "abc", 2: "bac", 3: "cba"}, {1: "a", 2: "b", 3: "c"})
        assert isNPE({1: "abc", 2: "abc", 3: "cba"}, {1: "b", 2: "a", 3: "c"}) is False
        assert isNPE({1: "abcdef", 2: "fedcba"}, {1: "ace", 2: "bdf"}) is False
        with pytest.raises(TypeError):
            isNPE({}, {1: "abcd", 2: "dcba"})
            isNPE({1: "abcdef", 2: "fedcba"}, {1: "ace"})
            isNPE({1: "ad", 2: "bc"}, {1: "b", 2: "a", 3: "c"})

    def test_getPPE_PEF(self):
        assert getPPE_PEF(6, 4, {1: "abcdef", 2: "adbcef", 3: "bacdfe", 4: "bacefd"}) == \
               {1: "a", 2: "df", 3: "b", 4: "ce"}
        assert getPPE_PEF(6, 4, {1: "abcdef", 2: "adbcef", 3: "bacdfe", 4: "efabdc"}) is None
        assert getPPE_PEF(6, 5, {1: "abcdef", 2: "adbcef", 3: "bacdfe", 4: "efabdc", 5: "dbacef"}) is None
