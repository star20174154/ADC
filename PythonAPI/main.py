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
        # control.run()

        # 此时使用决赛时候的代码，设置对应的Flag=True
        final_task = False

        if final_task:
            # 创建任务列表
            task_list = ['自动驾驶']
        else:
            task_list = ['前车静止', '紧急制动', '直线跟车', '前车阻碍', '自动驾驶']

        # 选择任务的序号
        task_num = 0
        task = task_list[task_num]

        print("========================")
        print("选择任务{}: {}".format(task_num, task_list[task_num]))
        print("========================")

        # 根据不同任务执行不同的算法
        if task_num == 0:
            control.run(0, final_task=final_task)
        elif task_num == 1:
            control.run(1, final_task=final_task)
        elif task_num == 2:
            control.run(2, final_task=final_task)
        else:
            print("没有'{}'任务,请将任务序号修改为0,1或2".format(task))

        # 停止平台
        ADCPlatform.stop()

    else:
        # 停止平台
        ADCPlatform.stop()
