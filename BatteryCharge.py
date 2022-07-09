import psutil, time, pyttsx3
from win10toast import ToastNotifier

if __name__ == "__main__":
    engine = pyttsx3.init()
    engine.setProperty('rate', 100)
    toast = ToastNotifier()
    battery = psutil.sensors_battery()
    charge_percents = range(10, 101, 10) #(10, 15, 25, 30, 40, 50, 75)
    check_time = 5
    curr_percent = 100
    running = True
    while running:
        battery = psutil.sensors_battery()
        time.sleep(check_time)
        if battery.percent in charge_percents and battery.percent != curr_percent:
                curr_percent = battery.percent
                toast.show_toast(
                    "Повідомлення",
                    f"Увага! Заряд акумулятора дорівнює {curr_percent}%",
                    duration = 100,
                    threaded = True,
                )
                engine.say(f"Warning! Battery charge is {curr_percent} percent")
                engine.runAndWait()
