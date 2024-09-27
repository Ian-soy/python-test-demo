import time
from datetime import datetime

# timestamp = datetime.now() # timestamp===> 2024-09-27 15:30:32.442887

timestamp = time.time() # timestamp===> 1727422196.4515572（秒）
milliseconds = int(timestamp * 1000)
print('timestamp===>', milliseconds) # timestamp===> 1727422423897（毫秒）