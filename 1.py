from gpiozero import OutputDevice
from time import sleep

# GPIO 32번 핀을 사용하여 릴레이를 제어합니다.
solenoid = OutputDevice(32)

try:
    while True:
        # 솔레노이드 켜기
        solenoid.on()
        print("솔레노이드 켜짐")
        sleep(1)  # 1초 대기
        
        # 솔레노이드 끄기
        solenoid.off()
        print("솔레노이드 꺼짐")
        sleep(1)  # 1초 대기

except KeyboardInterrupt:
    # Ctrl+C로 프로그램 종료 시 핀을 정리합니다.
    solenoid.off()
    print("프로그램 종료")
