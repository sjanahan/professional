# 20171219_qlecorre-fix-connection-manager-unit-tests  

## Pre-Review
### What will this Pull Request do?
Fix the unit tests that broke as a result of merging the refactor of connection manager

### Why is this Pull Request needed?
Broken unit tests will prevent deployment to stg/prod

### What's the *one* goal of this PR? (cleaning/refactoring/feature/bugfix)
Bugfix

### Are there any points in the code the reviewer needs to double check?
Make sure the unit tests pass

### Are there any Pull Requests open in other repos which need to be merged with this?
No

### What issues does this address? (Please link tickets)
No JIRA ticket

### Does the PR name match the standard?
  1. [x] Name includes ticket number
  2. [-] Name is categoried in path. For example: feature/BIG-1265

### Is the commit history squashed?
Yes

## Review
### [x] Pull down the code from the branch
### [x] Does it start/compile without modification?
### [-] Is it style compliant? (PEP8/Google/...)
### [] Read the code
###### 1. What parts of the code have been added/modified/deleted?
* Added: 
  1. Tests to genericize data source health checks because it started with only pre-aggs, but now includes engagement
* Modified:
  1. Some places video slices is now called engagement in the source code
* Deleted:

###### 2. What have you learned?
* Engagement is derived from video slices

###### 3. What inputs should be tested/might be troublesome?
* Default values for connection manager data fetches

###### 4. Any code smells?
### [-] Manually test the code
### [x] Run the unit tests
### [x] Run the integration tests
### [-] Run the coverage tests

## Post-Review
### What did you think of the PR overall?
Good. Thank you for fixing the unit tests!

### What would you suggest changing architecturally?
Nothing

### What could more optimal in this PR?
Nothing I can think of.

### What further testing would you suggest?
HEAD of develop unit test results:
```
Ran 168 tests in 3.213s

FAILED (failures=4, errors=10)
```

This branch
```
Ran 167 tests in 5.859s

OK
```

I got this output when running the unit tests which was concerning. Can you explain it?
```
Exception in thread Thread-1:
Traceback (most recent call last):
  File "/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/threading.py", line 914, in _bootstrap_inner
    self.run()
  File "/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/threading.py", line 862, in run
    self._target(*self._args, **self._kwargs)
  File "/Users/janahan/git/analytics-api/media/utils/polling_utils.py", line 131, in get_all_max_batch_seq_id
    connection_manager.assess_data_sources_health()
  File "/Users/janahan/git/analytics-api/media/utils/data_source_connection_manager.py", line 89, in assess_data_sources_health
    self._assess_health(PREAGGREGATES_DB)
  File "/Users/janahan/git/analytics-api/media/utils/data_source_connection_manager.py", line 129, in _assess_health
    if not self.spawn_connection_pool(name):
  File "/Users/janahan/git/analytics-api/media/utils/data_source_connection_manager.py", line 175, in spawn_connection_pool
    if self.pools[name]:
KeyError: 'TEST-PREAGGREGATES_DB'
```

Additionally, the following behave test is broken in HEAD of develop and in this branch:
```
Failing scenarios:
  v4/request-validation.feature:33  Test analytics_report request -- @1.16 requests
```

Will you fix it or make a ticket to track that work?
### Any other comments?
Nope
