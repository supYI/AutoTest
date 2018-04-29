import random
import unittest

from init import logging_info
from appium import webdriver
from ZJRCPay import ZJRCPay
from config.conf import desired_caps, EntryItem, ActivityCaps, para_dict
from selenium.common.exceptions import NoSuchElementException


class CPayLoop(unittest.TestCase):
    app = None

    @classmethod
    def setUpClass(cls):
        desiredCaps = {
            'platformName': desired_caps['platformName'],
            'platformVersion': desired_caps['platformVersion'],
            'deviceName': desired_caps['deviceName'],
            'appPackage': desired_caps['appPackage'],
            'appActivity': desired_caps['appActivity'],
            # 'appWaitActivity': desired_caps['appWaitActivity'],
            'newCommandTimeout': desired_caps['newCommandTimeout'],
            'noReset': desired_caps['noReset']
        }
        driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desiredCaps)
        # 默认查找界面元素最大时长设置为5秒
        driver.implicitly_wait(5)
        cls.app = ZJRCPay(driver)
        logging_info("拷机测试开始")

    def test_001_sign(self):
        logging_info('用例1：自动签到')

        self.app.auto_sign()
        if self.app.sign is None:
            logging_info('无需签到')
        else:
            self.assertEqual(self.app.sign, True, '自动签到失败')

    def test_002_manu_sign(self):
        logging_info('用例2：手动签到')

        self.app.manu_sign()
        self.assertEqual(self.app.result, '签到成功', '手动签到失败')

    def test_003_random_tap(self):
        logging_info('用例2：随机点击')

        if self.app.sign is not False:
            for i in range(para_dict['random_tap_cnt']):
                logging_info('第%s次随机点击事件' % (i + 1))
                self.app.random_tap()
                self.assertEqual(self.app.last_activity, ActivityCaps['Main'], '未返回到主界面')
        else:
            raise AssertionError('签到状态异常')

    def test_100_bank_card_entry(self):
        logging_info('用例100：银行卡消费')
        success_cnt = 0
        for i in range(para_dict['bank_trading_cnt']):
            amount = random.randint(1, 10000)
            self.app.trading_full(EntryItem['ic'], amount, passwd='123456')
            if self.app.result == '交易成功':
                logging_info('第%s笔：交易成功' % (i + 1))
                success_cnt += 1
                self.app.result_store()
            else:
                logging_info('第%s笔：交易失败' % (i + 1))
                self.app.result_store()
            logging_info('交易成功/交易总数：%s/%s' % (success_cnt, i + 1))

    def test_200_bank_card_entry(self):
        logging_info('用例200：免密消费')
        success_cnt = 0
        for i in range(para_dict['nonsecret_trading_cnt']):
            amount = random.randint(1, 1000)
            self.app.trading_full(EntryItem['non-secret'], amount, sign=False)
            if self.app.result == '交易成功':
                logging_info('第%s笔：交易成功' % (i + 1))
                success_cnt += 1
                self.app.result_store()
            else:
                logging_info('第%s笔：交易失败' % (i + 1))
                self.app.result_store()
            logging_info('交易成功/交易总数：%s/%s' % (success_cnt, i + 1))

    # def test_300_pjs(self):
    #     logging_info('用例300：手动批结算')
    #     self.assertRaises(NoSuchElementException, self.app.manu_pjs())

    @classmethod
    def tearDownClass(cls):
        cls.app.driver.quit()
