Librato BG
============


Allows for submitting of librato events in a background thread, heavily inspired by segment.io's python library which does the same.

Usage 
------

```python
from librato_bg import Client

# initialize with librato API tokens
self.client = Client(user, token)

# track as your normally would, params are event, value and source.
# This is non-blocking, submission will take place in other thread
self.client.gauge('user_clicked', 1, 'prod')

# when exiting, flush to join threads and make sure everything is sent
self.client.join()
