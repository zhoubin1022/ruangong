import unittest
from unittest import main
from unittest.mock import patch

import keyCount


class Test_Key(unittest.TestCase):
    def test_readFile(self):
        with patch('builtins.print') as mocked_print:
            keyCount.readFile('test.c', 1)
            mocked_print.assert_called_with("total num: ", 48)
            keyCount.readFile('test.c', 4)
            mocked_print.assert_called_with("if-elseif-else num: ", 1)


if __name__ == '__main__':
    main()
