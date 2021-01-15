import unittest
import perm_lex

class TestAssign1(unittest.TestCase):

    def test_perm_gen_lex(self):
        self.assertEqual(perm_lex.perm_gen_lex('ab'),['ab','ba'])
        self.assertEqual(perm_lex.perm_gen_lex(''),[])

if __name__ == "__main__":
        print(perm_lex.perm_gen_lex('abc'))
        unittest.main()
