import time
from px4flow import PX4FLOW

px4flow = PX4FLOW()

while (1):
	print px4flow.read()
	time.sleep(0.2)
	
