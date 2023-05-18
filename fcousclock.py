import time

def focus_timer(minutes):
    seconds = minutes * 60
    for i in range(seconds, 0, -1):
        print('Remaining time:', i // 60, 'min', i % 60, 'sec')
        time.sleep(1)
    print('Time is up! Good job focusing.')

focus_timer(25) # 25分钟专注时钟
