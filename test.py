#import helloworld
# message = "hello world"
# print(message)
import time
ticks = time.time()
print("Current time is: ",ticks)
localTime = time.localtime(ticks)
print(localTime)
strTime = time.asctime(localTime)
print(strTime)


