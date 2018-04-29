para_dict = {
    'random_tap_cnt': 0,              # 随机点击事件次数
    'bank_trading_cnt': 300,            # 消费循环次数
    'nonsecret_trading_cnt': 300,       # 免密循环次数
}

desired_caps = {
    'platformName': 'Android',
    'platformVersion': '5.1.1',
    'deviceName': '0123456789ABCDEF',
    'app': '',
    'appPackage': 'com.centerm.cpay.payment',
    'appActivity': '.activity.WelcomeActivity',
    'appWaitActivity': '.activity.MainActivity',
    'newCommandTimeout': '120',
    'noReset': True,
}

ActivityCaps = {
    'Welcome': '.activity.WelcomeActivity',
    'Trading': '.activity.TradingActivity',
    'Main': '.activity.MainActivity',
    'InputMoney': '.activity.InputMoneyActivity',
    'CheckCard': '.activity.CheckCardActivity',
    'InputPasswd': '.activity.InputPasswdActivity',
    'Esignatrue': '.activity.EsignatrueActivity',
    'Result': '.activity.ResultActivity',
}

pinPad = {
    '0': 'com.centerm.dev.pinpad:id/btn_key0',
    '1': 'com.centerm.dev.pinpad:id/btn_key1',
    '2': 'com.centerm.dev.pinpad:id/btn_key2',
    '3': 'com.centerm.dev.pinpad:id/btn_key3',
    '4': 'com.centerm.dev.pinpad:id/btn_key4',
    '5': 'com.centerm.dev.pinpad:id/btn_key5',
    '6': 'com.centerm.dev.pinpad:id/btn_key6',
    '7': 'com.centerm.dev.pinpad:id/btn_key7',
    '8': 'com.centerm.dev.pinpad:id/btn_key8',
    '9': 'com.centerm.dev.pinpad:id/btn_key9',
    'cancle': 'com.centerm.dev.pinpad:id/btn_key_cancel',
    'clear': 'com.centerm.dev.pinpad:id/btn_key_clear',
    'confirm': 'com.centerm.dev.pinpad:id/btn_key_confirm'
}

EntryItem = {
    'ic': 'bank_card_entry',
    'wx': 'wx_entry',
    'ali': 'ali_entry',
    'sign': [(90, 430)],
    'non-secret': [(270, 430)],
    # 'non-secret': [(100, 100)],
    'citizen': [(450, 430)],
    'point': [(90, 600)],
    'point-query': [(270, 600)],
    'fshl': [(450, 600)],
    'balance': [(90, 780)],
    'transfer': [(270, 780)],
    'bank-revoke': [(450, 780)],
    'scan-revoke': [(90, 430)],
    'pre-authorization': [(270, 430)],
    'trading-query': [(450, 430)],
    'sales-return': [(90, 600)],
    'pjs': [(270, 600)],
    'setting': [(450, 600)],
}

TradingType = {
    'scan': 'go_scan_pay',
    'code': 'go_code_pay',
}

ElementID = {
    'dialog_msg': 'dialog_message',
    'positive_btn': 'positive_btn',
    'negative_btn': 'negative_btn',
    'result_back_btn': 'result_back_btn',
    'title_show': 'title_show',
    'loading_tip_show': 'loading_tip_show',
    'number_pad_show3': 'number_pad_show3',
    'amt_confirm_btn': 'amt_confirm_btn',
    'confirm_btn': 'confirm_btn',
    'amount_show': 'amount_show',
    'entry_name_show': 'entry_name_show',
    'entry_top_name_show': 'entry_top_name_show',
    'back_btn': 'back_btn',
    'result_text': 'result_text',
    'card': 'bank_card_entry',
    'wx': 'wx_entry',
    'ali': 'ali_entry',
    'scan': 'go_scan_pay',
    'code': 'go_code_pay',
    'values': 'com.centerm.cpay.payment:id/value'
}
