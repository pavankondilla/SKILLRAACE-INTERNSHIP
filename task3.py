import time

def countdown_timer(seconds):
    while seconds:
        hrs, secs = divmod(seconds, 3600)
        mins, secs = divmod(secs, 60)
        timer = '{:02d}:{:02d}:{:02d}'.format(hrs, mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        seconds -= 1
    
    print("Time's up!")

# Example usage
if __name__ == "__main__":
    seconds = int(input("Enter the time in seconds: "))
    countdown_timer(seconds)
