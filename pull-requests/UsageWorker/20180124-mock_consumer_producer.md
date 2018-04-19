# 20180124-mock_consumer_producer by Sahil

## Pre-Review
### What will this Pull Request do?
Create a POC rabbit-mq consumer for pulling events from media service into usage db

### Why is this Pull Request needed?
To validate that rabbit-mq handles our use case of single events as well as batched upserts

### What's the *one* goal of this PR? (cleaning/refactoring/feature/bugfix)
Feature

### Are there any points in the code the reviewer needs to double check?
n/a

### Are there any Pull Requests open in other repos which need to be merged with this?
No

### What issues does this address? (Please link tickets)
AN-2128

### Does the PR name match the standard?
  1. [-] Name includes ticket number
  2. [-] Name is categoried in path. For example: feature/BIG-1265

### Is the commit history squashed?
No

## Review
### [x] Pull down the code from the branch
### [x] Does it start/compile without modification?
* the consumer/consumer_driver.py driver starts!
```bash
(analytics-usage-writer) janahan@Janahan-Temp ~here (mock_consumer_producer)$ python consumer/consumer_driver.py                                                                                                                                             [ruby-2.4.2p198]
/Users/janahan/venv/analytics-usage-writer/lib/python3.5/site-packages/jwplayer/config/config.py:229: UserWarning: Warning: could not load /Users/janahan/git/analytics-usage-writer/conf.d/local/config.yaml:
argument 'data' must be of type 'dict'
  warnings.warn("Warning: could not load {}:\n{}".format(cfgfile, e))
/Users/janahan/venv/analytics-usage-writer/lib/python3.5/site-packages/kombu/mixins.py:157: DeprecationWarning: The 'warn' method is deprecated, use 'warning' instead
  warn(W_CONN_ERROR, interval, exc, exc_info=1)
/Users/janahan/venv/analytics-usage-writer/lib/python3.5/site-packages/kombu/mixins.py:157: DeprecationWarning: The 'warn' method is deprecated, use 'warning' instead
  warn(W_CONN_ERROR, interval, exc, exc_info=1)
/Users/janahan/venv/analytics-usage-writer/lib/python3.5/site-packages/kombu/mixins.py:157: DeprecationWarning: The 'warn' method is deprecated, use 'warning' instead
  warn(W_CONN_ERROR, interval, exc, exc_info=1)
/Users/janahan/venv/analytics-usage-writer/lib/python3.5/site-packages/kombu/mixins.py:157: DeprecationWarning: The 'warn' method is deprecated, use 'warning' instead
  warn(W_CONN_ERROR, interval, exc, exc_info=1)
^Cbye bye
```

* the producer/producer_driver.py starts after fixing the command from the README
```
(analytics-usage-writer) janahan@Janahan-Temp ~here (mock_consumer_producer)$ python mock_producer/producer_driver.py --write-mode=CALLBACK                                                                                                                  [ruby-2.4.2p198]
/Users/janahan/venv/analytics-usage-writer/lib/python3.5/site-packages/jwplayer/config/config.py:229: UserWarning: Warning: could not load /Users/janahan/git/analytics-usage-writer/conf.d/local/config.yaml:
argument 'data' must be of type 'dict'
  warnings.warn("Warning: could not load {}:\n{}".format(cfgfile, e))
Executing cycle 1/10 of batch worker updating 1 rows per request every 1e-05 seconds

message handler being called with {'site': {'bytes_stored': 5, 'id': '-GQYSKGX'}}
{'site': {'bytes_stored': 5, 'id': '-GQYSKGX'}}
Executing cycle 2/10 of batch worker updating 1 rows per request every 1e-05 seconds

message handler being called with {'site': {'bytes_stored': 1, 'id': '-CQ0WYQG'}}
{'site': {'bytes_stored': 1, 'id': '-CQ0WYQG'}}
Executing cycle 3/10 of batch worker updating 1 rows per request every 1e-05 seconds

message handler being called with {'site': {'bytes_stored': 0, 'id': '-P0KVZSJ'}}
{'site': {'bytes_stored': 0, 'id': '-P0KVZSJ'}}
Executing cycle 4/10 of batch worker updating 1 rows per request every 1e-05 seconds

message handler being called with {'site': {'bytes_stored': 4, 'id': '-252FTR9'}}
{'site': {'bytes_stored': 4, 'id': '-252FTR9'}}
Executing cycle 5/10 of batch worker updating 1 rows per request every 1e-05 seconds

message handler being called with {'site': {'bytes_stored': 7, 'id': '-J3T5BL1'}}
{'site': {'bytes_stored': 7, 'id': '-J3T5BL1'}}
Executing cycle 6/10 of batch worker updating 1 rows per request every 1e-05 seconds

message handler being called with {'site': {'bytes_stored': 0, 'id': '-16168Y6'}}
{'site': {'bytes_stored': 0, 'id': '-16168Y6'}}
Executing cycle 7/10 of batch worker updating 1 rows per request every 1e-05 seconds

message handler being called with {'site': {'bytes_stored': 2, 'id': '-S5T2EUC'}}
{'site': {'bytes_stored': 2, 'id': '-S5T2EUC'}}
Executing cycle 8/10 of batch worker updating 1 rows per request every 1e-05 seconds

message handler being called with {'site': {'bytes_stored': 6, 'id': '-883R485'}}
{'site': {'bytes_stored': 6, 'id': '-883R485'}}
Executing cycle 9/10 of batch worker updating 1 rows per request every 1e-05 seconds

message handler being called with {'site': {'bytes_stored': 4, 'id': '-F8XOPEM'}}
{'site': {'bytes_stored': 4, 'id': '-F8XOPEM'}}
Executing cycle 10/10 of batch worker updating 1 rows per request every 1e-05 seconds

message handler being called with {'site': {'bytes_stored': 10, 'id': '-5AAHK5K'}}
{'site': {'bytes_stored': 10, 'id': '-5AAHK5K'}}
Executing cycle 1/5 of batch worker updating 1 rows per request every 1e-05 seconds

message handler being called with {'site': {'media_count': 6, 'id': '-FKDGETV'}}
{'site': {'media_count': 6, 'id': '-FKDGETV'}}
Executing cycle 2/5 of batch worker updating 1 rows per request every 1e-05 seconds

message handler being called with {'site': {'media_count': 0, 'id': '-VPRU2ZW'}}
{'site': {'media_count': 0, 'id': '-VPRU2ZW'}}
Executing cycle 3/5 of batch worker updating 1 rows per request every 1e-05 seconds

message handler being called with {'site': {'media_count': 8, 'id': '-WACIIK2'}}
{'site': {'media_count': 8, 'id': '-WACIIK2'}}
Executing cycle 4/5 of batch worker updating 1 rows per request every 1e-05 seconds

message handler being called with {'site': {'media_count': 1, 'id': '-OC5TRTH'}}
{'site': {'media_count': 1, 'id': '-OC5TRTH'}}
Executing cycle 5/5 of batch worker updating 1 rows per request every 1e-05 seconds

message handler being called with {'site': {'media_count': 10, 'id': '-3HOU8SF'}}
{'site': {'media_count': 10, 'id': '-3HOU8SF'}}
```

* The docker container ran no problem! It didn't have any output due to the `-d` flag
* The mock_producer/producer_driver.py also ran as is
```bash
(analytics-usage-writer) janahan@Janahan-Temp ~here (mock_consumer_producer)$ python mock_producer/producer_driver.py --write-mode=PUBSUB                                                                                                                    [ruby-2.4.2p198]
/Users/janahan/venv/analytics-usage-writer/lib/python3.5/site-packages/jwplayer/config/config.py:229: UserWarning: Warning: could not load /Users/janahan/git/analytics-usage-writer/conf.d/local/config.yaml:
argument 'data' must be of type 'dict'
  warnings.warn("Warning: could not load {}:\n{}".format(cfgfile, e))
Executing cycle 1/10 of batch worker updating 1 rows per request every 1e-05 seconds

v1.site.media_library.-O0MYOSE.-.storage_changed.-
Executing cycle 2/10 of batch worker updating 1 rows per request every 1e-05 seconds

v1.site.media_library.-HCZKIT9.-.storage_changed.-
Executing cycle 3/10 of batch worker updating 1 rows per request every 1e-05 seconds

v1.site.media_library.-KFVM3F7.-.storage_changed.-
Executing cycle 4/10 of batch worker updating 1 rows per request every 1e-05 seconds

v1.site.media_library.-PLBTR0Q.-.storage_changed.-
Executing cycle 5/10 of batch worker updating 1 rows per request every 1e-05 seconds

v1.site.media_library.-JVWFGLK.-.storage_changed.-
Executing cycle 6/10 of batch worker updating 1 rows per request every 1e-05 seconds

v1.site.media_library.-PUIOHH8.-.storage_changed.-
Executing cycle 7/10 of batch worker updating 1 rows per request every 1e-05 seconds

v1.site.media_library.-RL4YKUS.-.storage_changed.-
Executing cycle 8/10 of batch worker updating 1 rows per request every 1e-05 seconds

v1.site.media_library.-WSSD6KZ.-.storage_changed.-
Executing cycle 9/10 of batch worker updating 1 rows per request every 1e-05 seconds

v1.site.media_library.-ESQ98WL.-.storage_changed.-
Executing cycle 10/10 of batch worker updating 1 rows per request every 1e-05 seconds

v1.site.media_library.-GWUHENY.-.storage_changed.-
Executing cycle 1/5 of batch worker updating 1 rows per request every 1e-05 seconds

v1.site.media_library.-YH2MJ0J.-.storage_changed.-
Executing cycle 2/5 of batch worker updating 1 rows per request every 1e-05 seconds

v1.site.media_library.-2MKIL7W.-.storage_changed.-
Executing cycle 3/5 of batch worker updating 1 rows per request every 1e-05 seconds

v1.site.media_library.-2PIM5ED.-.storage_changed.-
Executing cycle 4/5 of batch worker updating 1 rows per request every 1e-05 seconds

v1.site.media_library.-P05BC9W.-.storage_changed.-
Executing cycle 5/5 of batch worker updating 1 rows per request every 1e-05 seconds

v1.site.media_library.-VTHMX4G.-.storage_changed.-
```


### [-] Is it style compliant? (PEP8/Google/...)
### [x] Read the code
###### 1. What parts of the code have been added/modified/deleted?
* Added:
    1. A mock consumer
    2. A mock producer in two modes
        1. CALLBACK - doesn't have additional dependencies
        2. PUBSUB - involves a dockerized rabbit mq server 
* Modified:
* Deleted:

###### 2. What have you learned?
* Not all queue'ing systems have easily flexible pulling semantics

###### 3. What inputs should be tested/might be troublesome?
* Ratcheting up the message batch size to see if the DB or consumer fails first

###### 4. Any code smells?
* 

### [x] Manually test the code
### [-] Run the unit tests
### [-] Run the integration tests
### [-] Run the coverage tests

## Post-Review
### What did you think of the PR overall?
The code organization makes it easy to follow. I like it overall!

### What would you suggest changing architecturally?
I'd move all source files other than the drivers in mock_consumer and producer into their own respective lib directories

### What could more optimal in this PR?
Not too much. Seems pretty clean to me

### What further testing would you suggest?
Is there any enforcement on the shape of the messages in the queue? Would upstream changes break our consumers?

### Any other comments?
* Please reference AN-2128 in the ticket
* Please squash the commit history before we merge. I can show you how I do it if you'd like!
* I am getting the following message when I start any process in the repo. Is this expected?
```
/Users/janahan/venv/analytics-usage-writer/lib/python3.5/site-packages/jwplayer/config/config.py:229: UserWarning: Warning: could not load /Users/janahan/git/analytics-usage-writer/conf.d/local/config.yaml:
argument 'data' must be of type 'dict'
``` 
* What is the login for the rabbitmq UI? Could you share it via Lastpass with the team?
