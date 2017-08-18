from example.task1 import task1_1
import time

args = (1, 2, 3)
kwargs = {'a': 1, 'b': 2}
result = task1_1.delay(*args, **kwargs)
print 'ready >>> ',result.ready()
time.sleep(12)
print 'ready >>> ',result.ready()
print 'get >>> ',result.get(timeout=1)