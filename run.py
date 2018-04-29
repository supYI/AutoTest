import unittest
from cases.CPayLoopTest import CPayLoop
from cases.CPayTestCase import CPayTestCase

while 1:
    # arg = input('【1】为拷机测试，【2】为单元测试，请输入对应数字：')
    arg = '1'
    if arg == '1':
        print('测试程序启动中.....')
        suite = unittest.TestLoader().loadTestsFromTestCase(CPayLoop)
        suite = unittest.TestSuite([suite, ])
        unittest.TextTestRunner(verbosity=2).run(suite)
        break
    elif arg == '2':
        suite = unittest.TestLoader().loadTestsFromTestCase(CPayTestCase)
        suite = unittest.TestSuite([suite, ])
        unittest.TextTestRunner(verbosity=2).run(suite)
        break
    else:
        print('操作有误，请重新输入：【1】为单元测试，【2】为拷机测试 ：')
