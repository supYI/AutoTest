from config.conf import EntryItem, ElementID, pinPad, ActivityCaps
from selenium.common.exceptions import NoSuchElementException
from appium.webdriver.webdriver import WebDriver
from init import logging_info, logging_error, project_dir
import time
import random
import csv


class ProcessCancle(Exception):
    ''' 自定义交易中止异常'''

    def __init__(self, msg):
        Exception.__init__(self, msg)


class ZJRCPay(object):

    def __init__(self, driver):
        self.driver = driver    # type: WebDriver
        self.result = None  # 交易结果：成功OR失败
        self.values = []    # 交易结果返回值
        self.sign = None    # 签名标识位：None为未签到状态，True为签到失败，False为签到失败
        self.amount = None  # 消费金额
        self.last_activity = None   # 原先Activity
        self.width = self.driver.get_window_size()['width']     # 屏幕宽度
        self.height = self.driver.get_window_size()['height']   # 屏幕高度

    # 获取当前界面
    @property
    def current_activity(self):
        return self.driver.current_activity

    # 保存交易结果
    def result_store(self):
        if self.values is not None:
            logging_info('开始保存交易结果')
            if self.result == "交易成功":
                with open(project_dir + '\\data\\trading_list_info.csv', 'a+', newline='', encoding='gbk') as f:
                    writer = csv.writer(f)
                    writer.writerow(self.values)
            else:
                with open(project_dir + '\\data\\fail_reason_info.csv', 'a+', newline='', encoding='gbk') as f:
                    writer = csv.writer(f)
                    writer.writerow(self.values)

            logging_info('保存本次结果完毕')

    # 封装源码查找方法
    def page_source_find(self, reg_string):
        return self.driver.page_source.find(reg_string)

    # 封装back方法
    def back(self):
        self.driver.back()

    # 封装swipe方法
    def swipe(self, start_x, start_y, end_x, end_y, duration=None):
        self.driver.swipe(start_x, start_y, end_x, end_y, duration=duration)

    # 等待有新界面跳转
    def activity_wait(self, activity):
        logging_info('当前界面是：' + activity)

        while self.current_activity == activity:
            pass

    # 封装获取元素方法
    def find_element(self, element_ID):
        try:
            return self.driver.find_element_by_id(element_ID)
        except NoSuchElementException:
            logging_error('找不到对应的元素')

    # 封装获取元素方法（复数）
    def find_elements(self, element_ID):
        try:
            return self.driver.find_elements_by_id(element_ID)
        except NoSuchElementException:
            logging_error('找不到对应的元素')

    # 封装click方法
    def click_element(self, element):
        element = self.find_element(element)

        try:
            element.click()
        except AttributeError:
            logging_error('AttributeError occured')

    # 封装tap方法
    def tap_element(self, positions, duration=100):
        self.driver.tap(positions, duration=duration)

    # 获取元素属性
    def get_attribute(self, element_ID, attribute='text'):
        element = self.find_element(element_ID)

        try:
            return element.get_attribute(attribute)
        except AttributeError:
            logging_error('AttributeError occured')

    # 获取元素属性（复数）
    def get_attributes(self, element_ID, attribute='text'):
        elements = self.find_elements(element_ID)

        try:
            return [i.get_attribute(attribute) for i in elements]
        except AttributeError:
            logging_error('AttributeError occured')

    # 选择交易通道
    # ic：消费，wx：微信，ali：支付宝
    # 由于子图标元素无合适的方法定位，暂采取点击指定坐标，并根据实际情况修改conf.py文件
    def trading_entry(self, entry):
        assert self.current_activity == ActivityCaps['Main'], '跳转到主界面失败'

        logging_info('进入交易通道')
        if entry == EntryItem['ic'] or entry == EntryItem['wx'] or entry == EntryItem['ali']:
            self.click_element(entry)
        else:
            self.tap_element(entry)

    # 输入金额
    def amount_input(self, amount=None):
        assert self.current_activity == ActivityCaps['InputMoney'], '跳转到金额界面失败'

        self.amount = None

        logging_info('进入金额')

        # 等待元素定位
        while len(self.find_elements(ElementID['number_pad_show3'])) != 12:
            logging_info("不足12元素")
            if self.current_activity != ActivityCaps['InputMoney']:
                raise ProcessCancle('交易中止')

        num_pad = self.find_elements(ElementID['number_pad_show3'])

        try:
            # 是否输入金额
            if amount is not None:
                logging_info('输入金额为：%s' % amount)
                for i in str(amount):
                    if self.current_activity == ActivityCaps['InputMoney']:
                        if i != '0':
                            num_pad[int(i) - 1].click()
                        else:
                            num_pad[10].click()
                    else:
                        raise ProcessCancle('交易中止')
                self.amount = self.get_attribute(ElementID['amount_show'])
        except AttributeError:
            logging_error('AttributeError occured')

    def amount_clear(self, amount):
        assert self.current_activity == ActivityCaps['InputMoney'], '跳转到金额界面失败'

        # 等待元素定位
        while len(self.find_elements(ElementID['number_pad_show3'])) != 12:
            pass

        num_pad = self.find_elements(ElementID['number_pad_show3'])

        try:
            # 是否输入金额
            if amount is not None:
                logging_info('待清除金额为：%s' % amount)
                for i in range(len(amount)):
                    if self.current_activity == ActivityCaps['InputMoney']:
                        num_pad[11].click()
                    else:
                        raise ProcessCancle('交易中止')
                self.amount = self.get_attribute(ElementID['amount_show'])
        except AttributeError:
            logging_error('AttributeError occured')

    # 检卡：时间不可控，有时立即返回到输密界面，暂不做断言
    def card_check(self):
        # assert self.current_activity == ActivityCaps['CheckCard'], '跳转到检卡界面失败'

        if self.current_activity == ActivityCaps['CheckCard']:
            logging_info('进入检卡')
            self.activity_wait(ActivityCaps['CheckCard'])

            if self.current_activity == ActivityCaps['Main']:
                logging_info('检卡失败，返回到主界面')
                raise ProcessCancle('交易中止')

    # 输密
    def passwd_input(self, passwd=None):
        assert self.current_activity == ActivityCaps['InputPasswd'], '跳转到输密界面失败'

        logging_info('进入输密')
        for i in passwd:
            if self.current_activity == ActivityCaps['InputPasswd']:
                self.click_element(pinPad[i])
            else:
                raise ProcessCancle('交易中止')

    # 平台交互：时间不可控，有时立即返回到交易结果界面，暂不做断言
    def trading_interact(self):
        # assert self.current_activity == ActivityCaps['Trading'], '跳转到平台交互界面失败'

        if self.current_activity == ActivityCaps['Trading']:
            logging_info('正在与平台交互')
            self.activity_wait(ActivityCaps['Trading'])

    # 签名
    def signature(self):
        assert self.current_activity == ActivityCaps['Esignatrue'], '跳转到签名界面失败'

        logging_info('输入签名：FY')
        self.swipe(self.width * 0.2, self.height * 0.4,
                   self.width * 0.4, self.height * 0.4, 500)
        self.swipe(self.width * 0.2, self.height * 0.5,
                   self.width * 0.4, self.height * 0.5, 500)
        self.swipe(self.width * 0.2, self.height * 0.4,
                   self.width * 0.2, self.height * 0.65, 500)

        self.swipe(self.width * 0.6, self.height * 0.4,
                   self.width * 0.7, self.height * 0.5, 500)
        self.swipe(self.width * 0.8, self.height * 0.4,
                   self.width * 0.7, self.height * 0.5, 500)
        self.swipe(self.width * 0.7, self.height * 0.49,
                   self.width * 0.7, self.height * 0.65, 500)

    # 取消打印
    def printer_cancel(self, is_print=False):
        assert self.current_activity == ActivityCaps['Result'], '跳转到交易结果界面失败'

        logging_info('取消打印')
        if is_print is False:
            while self.current_activity == ActivityCaps['Result']:
                if self.page_source_find('交易失败') != -1:
                    break
                elif self.page_source_find('打印机') != -1:
                    self.click_element(ElementID['negative_btn'])
                    break

    # 交易结果页展示
    def get_result_info(self):
        assert self.current_activity == ActivityCaps['Result'], '跳转到交易结果界面失败'

        logging_info('获取结果页信息')
        self.result = self.get_attribute(ElementID['result_text'])

        if self.get_attribute(ElementID['title_show']) != '操作成功':
            self.values = self.get_attributes(ElementID['values'])

    # 自主签到结果
    def auto_sign(self):
        # assert self.current_activity == ActivityCaps['Trading'], '当前界面不是交易界面'
        # self.sign = None

        self.activity_wait(ActivityCaps['Welcome'])
        time.sleep(1)
        if self.current_activity == ActivityCaps['Trading']:
            self.activity_wait(ActivityCaps['Trading'])

            self.sign = True if self.get_attribute('dialog_message') == '自动签到成功' else False
            self.click_element('positive_btn')

    # 进行手动签到
    def manu_sign(self):
        assert self.current_activity == ActivityCaps['Main'], '当前界面不是主界面'

        self.result = None
        self.tap_element(EntryItem['sign'])
        # 等待交易结果页展示
        self.activity_wait(ActivityCaps['Trading'])
        self.get_result_info()

        if self.sign is False:
            if self.result == '签到成功':
                self.sign = True
        self.back()
        time.sleep(1)

    # 随机点击
    def random_tap(self, duration=100):
        assert self.current_activity == ActivityCaps['Main'], '当前界面不是主界面'

        self.last_activity = self.current_activity

        x = random.randint(1, self.width - 1)
        y = random.randint(self.height // 18, self.height - 1)

        self.tap_element([(x, y)], duration=duration)
        time.sleep(1)
        if self.current_activity != self.last_activity:
            if self.current_activity == ActivityCaps['Trading']:
                self.activity_wait(ActivityCaps['Trading'])

            time.sleep(1)
            self.back()

    # 手动批结算
    def manu_pjs(self):
        assert self.current_activity == ActivityCaps['Main'], '当前界面不是主界面'

        logging_info('向左边滑动屏幕')
        self.swipe(self.width * 0.7, self.height * 0.7,
                   self.width * 0.3, self.height * 0.7, 300)
        time.sleep(1)
        logging_info('点击批结算')
        self.tap_element(EntryItem['pjs'])
        self.click_element('positive_btn')

        while self.current_activity == ActivityCaps['Main']:
            if self.page_source_find('negative_btn') == -1:
                pass
            else:
                self.click_element('negative_btn')
                time.sleep(1)
                break

    # 银行卡完整交易拷机
    def trading_full(self, entry, amount, passwd=None, sign=True, printer=False):
        logging_info('----------交易开始----------')

        self.result = None
        self.values = None
        is_screenshot = False  # 是否已截屏，默认为否，一笔交易只截取一次

        try:
            # 进行交易前提：签到状态正常，当前界面为主界面
            if self.sign is False:
                raise AssertionError('签到状态异常，交易中止')

            while self.current_activity != ActivityCaps['Main']:
                logging_info('当前界面不是主界面,下次检测时间：50s后')

                if not is_screenshot:
                    self.driver.save_screenshot(
                        time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time())) + '.png')
                    is_screenshot = True
                time.sleep(50)

            logging_info('当前Activity为主界面，开始进行交易')
            self.trading_entry(entry)
            self.activity_wait(ActivityCaps['Main'])

            self.amount_input(amount)
            self.click_element(ElementID['amt_confirm_btn'])
            self.activity_wait(ActivityCaps['InputMoney'])

            self.card_check()

            if passwd:
                self.passwd_input(passwd)

                self.click_element(pinPad['confirm'])
                self.activity_wait(ActivityCaps['InputPasswd'])
            else:
                logging_info('无需输密')

            self.trading_interact()

            # 签名且跳转到签名页，进行签名；
            # 签名且跳转到交易结果页，说明交易有异常，获取交易结果；
            # 签名且跳转到其他界面，不做处理，self.result为None
            # 不签名且跳转到交易结果页，获取交易结果
            # 其他情况不做处理，默认结果为None
            if sign is True:
                if self.current_activity == ActivityCaps['Esignatrue']:
                    self.signature()
                    self.click_element(ElementID['confirm_btn'])
                    self.activity_wait(ActivityCaps['Esignatrue'])

                    self.printer_cancel()
                    self.get_result_info()
                    self.back()
                elif self.current_activity == ActivityCaps['Result']:
                    self.get_result_info()
                    self.back()
            elif sign is False:
                if self.current_activity == ActivityCaps['Result']:
                    self.printer_cancel()
                    self.get_result_info()
                    self.back()
            else:
                logging_info('需要签名，但未跳转到签名或跳转到交易结果页时出错')
        except ProcessCancle as e:
            logging_error(e)
