import alarmClock
import time
def main():

    print('*'*30)
    # Create an object from AlarmClock class
    ac_monday = alarmClock.AlarmClock(7, 15, 0)
    # Display the time
    print(ac_monday)

    # Set the alarm time
    ac_monday.set_alarm_time(7,16)
    # Display the time
    print(ac_monday)

    # Set alarm on
    ac_monday.set_alarm_on();
    print(ac_monday)

    if ac_monday.get_alarm_is_set() == True:

        # Converting the current time in seconds
        current_sec = ac_monday.convert_current_time_to_sec()
        print("Current time in seconds", current_sec)

        # Converting alarm time in seconds
        alarm_sec = ac_monday.conbert_alarm_time_to_sec()
        print("Current time in seconds", alarm_sec)