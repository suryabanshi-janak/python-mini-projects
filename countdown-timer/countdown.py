import time

def countdown(t):
  while t:
    mins, sec = divmod(t, 60) # returns a tuple containing the quotient and remainder of the division of t by 604

    timer = '{:02d}:{:02d}'.format(mins, sec) # formats the minutes and seconds into a string with leading zeros, ensuring that the timer is displayed in the format "MM:SS"

    print(timer, end='\r') # '\r' is the carriage return character. Unlike the newline character ('\n'), the carriage return character moves the cursor back to the beginning of the line without advancing to the next line. This creates the effect of overwriting the current line with the next printed content
    
    time.sleep(1) # pauses the execution of the program for 1 second, creating the one-second interval for the countdown
    t -= 1

  print('Countdown completed!')

input_time = input('Enter the time in seconds: ')
countdown(int(input_time))