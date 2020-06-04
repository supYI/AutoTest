环境依赖：
	操作环境：				windows
	python：				3.0以上
	Appium-Python-Client：	0.24
	Appium-Desktop:			1.3.1


运行方法：
1、将AppiumTest文件夹，拷贝到本地磁盘合适位置
2、命令行下，切换到AppiumTest根目录，根据实际参数修改conf.py文件，比如循环次数、子通道对应坐标等待，输入python run.py即可，或输入python run.py的绝对路径
3、根据提示，选择进行拷机测试or单元测试
PS：拷机测试是循环进行随机点击、消费和小额免密，单元测试单次执行收单基本流程，由于手动测试效率更高些，暂不作单元测试
