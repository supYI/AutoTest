import time
import random
import unittest

from init import logging_info
from appium import webdriver
from ZJRCPay import ZJRCPay
from config.conf import desired_caps, EntryItem, ActivityCaps
from selenium.common.exceptions import NoSuchElementException


class CPayTestCase(unittest.TestCase):
    pass

#     app = None

#     @classmethod
#     def setUpClass(cls):
#         desiredCaps = {
#             'platformName': desired_caps['platformName'],
#             'platformVersion': desired_caps['platformVersion'],
#             'deviceName': desired_caps['deviceName'],
#             'appPackage': desired_caps['appPackage'],
#             'appActivity': desired_caps['appActivity'],
#             # 'appWaitActivity': desired_caps['appWaitActivity'],
#             'newCommandTimeout': desired_caps['newCommandTimeout'],
#             'noReset': desired_caps['noReset']
#         }
#         driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desiredCaps)
#         # 默认查找界面元素最大时长设置为5秒
#         driver.implicitly_wait(5)
#         cls.app = ZJRCPay(driver)
#         logging_info("单元测试开始")

#     def test_001_sign(self):
#         logging_info('用例1：自动签到')
#         self.app.auto_sign()
#         if self.app.sign == '无需签到':
#             logging_info('无需签到')
#         else:
#             self.assertEqual(self.app.sign, '自动签到成功', '自动签到失败')

#     def test_002_manu_sign(self):
#         logging_info('用例2：手动签到')

#         self.app.manu_sign()
#         self.assertEqual(self.app.result, '签到成功', '手动签到失败')

#     def test_003_input_and_back(self):
#         logging_info('用例3：金额界面&返回')

#         entry_list = [EntryItem['ic'], EntryItem['wx'], EntryItem['ali']]

#         for entry in entry_list:
#             self.app.trading_entry(entry)
#             self.app.back()
#             time.sleep(1)

#             self.assertEqual(self.app.current_activity, ActivityCaps['Main'], '未返回到主界面')

#     def test_004_check_card_and_back(self):
#         amount

#     def test_004_amount_input_and_clear(self):
#         logging_info('用例4：金额输入&删除')
#         self.app.trading_entry(EntryItem['ic'])

#         amount = random.randint(1, 999999999)
#         # 输入金额
#         self.app.amount_input(amount)
#         self.assertEqual(self.app.amount, str(amount / 100), '输入金额和显示金额不相等')         # 清除金额

#         self.app.amount_clear(amount)
#         self.assertEqual(self.app.amount, '0.00', '金额清除失败')

#     def test_005_card_check_and_back(self):
#         logging_info('用例5：检卡&返回')

#     def test_006_wx_scan_and_back(self):
#         logging_info('')

#     def test_007_ali_scal_and_back(self):
#         logging_info('')

#     def test_008_wx_QR_and_cancle(self):
#         logging_info('')

#     def test_009_ali_QR_and_cancle(self):
#         logging_info('')

#     def test_100_bank_card_entry(self):
#         logging_info('用例100：银行卡消费')
#         success_cnt = 0
#         for i in range(300):
#             amount = random.randint(1, 10000)
#             self.app.trading_full(EntryItem['ic'], amount, '123456')
#             if self.app.result == '交易成功':
#                 logging_info('第%s笔：交易成功' % (i + 1))
#                 success_cnt += 1
#             else:
#                 logging_info('第%s笔：交易失败' % (i + 1))
#         logging_info('交易成功/交易总数：%s/%s' % (success_cnt, i + 1))

#     def test_200_bank_card_entry(self):
#         logging_info('用例200：免密消费')
#         success_cnt = 0
#         for i in range(200):
#             amount = random.randint(1, 1000)
#             self.app.trading_full(EntryItem['non-secret'], amount, sign=False)
#             if self.app.result == '交易成功':
#                 logging_info('第%s笔：交易成功' % (i + 1))
#                 success_cnt += 1
#             else:
#                 logging_info('第%s笔：交易失败' % (i + 1))
#         logging_info('交易成功/交易总数：%s/%s' % (success_cnt, i + 1))

#     def test_300_pjs(self):
#         logging_info('用例300：手动批结算')
#         self.assertRaises(NoSuchElementException, self.app.manu_pjs())

#     @classmethod
#     def tearDownClass(cls):
#         cls.app.driver.quit()
