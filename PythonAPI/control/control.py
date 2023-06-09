import ADCPlatform
import time


# 启动算法  在此方法中调用实现算法控制代码
def run():
    running = True
    # 毫米波真值传感器id
    radarId = 0
    # 摄像机传感器id
    cameraId = 0
    # 车道线传感器id
    landLineId = 0

    print("当前车辆安装传感器为")
    sensors = ADCPlatform.get_sensors()
    for sensor in sensors:
        if sensor.Name == "毫米波雷达":
            radarId = sensor.ID
        elif sensor.Name == "摄像机":
            cameraId = sensor.ID
        elif sensor.Name == "车道线传感器":
            landLineId = sensor.ID
        print("名称：" + sensor.Name + ",ID:" + str(sensor.ID))
    while running:
        # 获取车辆控制数据包
        control_data_package = ADCPlatform.get_control_data()
        if not control_data_package:
            print("任务结束")
            running = False
            break
        fs = control_data_package.json['FS']
        print("当前车车速：" + str(fs))
        # 获取图片数据包 10102为摄像机类型传感器id
        # image_package = ADCPlatform.get_image(cameraId)
        # 获取数据包 10101为雷达GPS等数据类型传感器id
        landLine_package = ADCPlatform.get_data(landLineId)
        # if landLine_package and len(landLine_package.json) > 0:
            # print(landLine_package.json)
        # data_package = ADCPlatform.get_data(radarId)
        # if data_package and len(data_package.json) > 0:
        #     print(data_package.json)
        #     ttc = 0
        #     if fs != 0:
        #         ttc = data_package.json[0]["Range"]/100/fs
        #     print(ttc)
        #     if data_package.json[0]["Range"] < 3500 and ttc < 3:
        #         ADCPlatform.control(0, 0, 1,0)
        #         print("break")
        #     # else:
        #         # ADCPlatform.control(0.7, 0, 0)
        # ADCPlatform.control(0.7, 0, 0,1)
        ADCPlatform.control(0.7, 0, 0,-1)
        # print("brake")

        # 休眠30毫秒
        # time.sleep(0.003)
