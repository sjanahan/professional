# 2017113_qelecorre-framework

## Pre-Review
### What will this Pull Request do?
* Create a docker container for redis
* Create a docker container for the worker itself
* Add logging 

### Why is this Pull Request needed?
So we can rip the logic of synchronizing tables within data sources out of the reporting API

### What's the *one* goal of this PR? (cleaning/refactoring/feature/bugfix)
Feature. Add preaggregates metadata to redis.

### Are there any points in the code the reviewer needs to double check?
Time zone tomfoolery

### Are there any Pull Requests open in other repos which need to be merged with this?
No

### What issues does this address? (Please link tickets)
AN-2171

### Does the PR name match the standard?
  1. [x] Name includes ticket number
  2. [] Name is categoried in path. For example: feature/BIG-1265.
  	* No, it does not include that it is a feature in the name of the branch.

### Is the commit history squashed?
* No. There are 6 commits.

## Review
### [x] Pull down the code from the branch
### [x] Does it start/compile without modification?
### [-] Is it style compliant? (PEP8/Google/...)
### [x] Read the code
###### 1. What parts of the code have been added/modified/deleted?
* Added:
	* A base class for MetadataGetter
	* An implementation for Preaggregates DB
	* A base class for MetadataSetter
	* An implementation for Redis 
* Modified:
* Deleted:

###### 2. What have you learned?
* `type` is a good unix cmd to see the definition of a bash alias
* redis stores objects as strings

###### 3. What inputs should be tested/might be troublesome?
* Edge cases of latest times for the batch and daily tables

###### 4. Any code smells?
### [x] Manually test the code
### [-] Run the unit tests
### [-] Run the integration tests
### [-] Run the coverage tests

## Post-Review
### What did you think of the PR overall?
I really like how simple the main function is. 

### What would you suggest changing architecturally?
I really like the class structure. Good use of a base class for MetadataGetter.

### What could more optimal in this PR?
Do you think that the worker should be responsible for synchronizing or just raw data fetching?

I could see a world where this worker does that kind of logic so the reporting API just fetches synchronized values instead of raw. This way we can isolate testing of the different edge cases into this service.


### What further testing would you suggest?
*I would suggest creating unit tests to simulate the scenarios that the synchronization of data sources is supposed to solve. When they overlap, when they don't, when one isn't working.

* Can we add testing for the timezone logic?

### Any other comments?
* Please upgrade the version of jwplayer-config!
* Can you squash the commit history before merging?
