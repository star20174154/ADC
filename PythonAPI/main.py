import ADCPlatform
import control


if __name__ == '__main__':
    # 开启平台SDK
    # 设置服务器访问地址
    serverUrl = 'http://www.adchauffeur.cn/api/'
    # 设置登录用户名
    username = 'NEU408_2'
    # 设置登录密码
    password = '123456'
    result = ADCPlatform.start(serverUrl, username, password)
    if result:
        print("算法接入成功！")
        print("启动任务")
        ADCPlatform.start_task()
        # 启动算法接入任务控制车辆
        control.run()

        # 停止平台
        ADCPlatform.stop()

    else:
        # 停止平台
        ADCPlatform.stop()
