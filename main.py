from time import time
from pioneer_sdk import Pioneer

mini = Pioneer()

class LogFilesUpdater():

    def __init__(self):
        self.file_name = 'latest.log'
        self.curr_cnt_str = 0
        self.old_curr_cnt_str = 0

        file = open(self.file_name, 'r')
        file_str = file.read().split('\n')
        self.curr_cnt_str = len(file_str)
        self.old_curr_cnt_str = self.curr_cnt_str
        file.close()
    
    def process(self):
        timer = time()

        while True:
            curr_time = time()
            if curr_time - timer > 1: # раз в секунду
                # открываем файл
                file = open(self.file_name, 'r')

                if file:
                    file_str = file.read().split('\n')
                    self.curr_cnt_str = len(file_str)

                    if self.curr_cnt_str > self.old_curr_cnt_str:
                        for idx in range(self.old_curr_cnt_str, self.curr_cnt_str):
                            if 'arm' in file_str[idx].split(' '):
                                mini.arm()
                                print('arm')
                            elif 'disarm' in file_str[idx].split(' '):
                                mini.disarm()
                                print('disarm')
                            elif 'white' in file_str[idx].split(' '):
                                mini.led_control(255, 1, 1, 1)
                                print('white')
                        self.old_curr_cnt_str = self.curr_cnt_str

                file.close()
                # читаем количество строк
                
                timer = time()


if __name__ == '__main__':
    log = LogFilesUpdater()
    log.process()