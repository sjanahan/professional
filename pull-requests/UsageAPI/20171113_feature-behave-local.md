# 20171113_feature/behave-local by Janahan

## Pre-Review
### What will this Pull Request do?
* Make behave tests for v1 and v2 work on a clean local db
* Add behave tests for v3 for test-data endpoints

### Why is this Pull Request needed?
* To facilitate iteration speed for developing on usage api. Part of SOA initiative

### Are there any points in the code the reviewer needs to double check?
* Make sure the unit tests and behave tests in all versions are passing

### Are there any Pull Requests open in other repos which need to be merged with this?
* No

### What issues does this address? (Please link tickets)
* AN-2108

### Does the PR name match the standard?
* Yes, uses the imperative tense

### Is the commit history squashed?
* Yes

## Review
### [x] Pull down the code from the branch
### [x] Does it start/compile without modification?
### [-] Is it style compliant? (PEP8/Google/...)
### [] Read the code
###### 1. What parts of the code have been added/modified/deleted?
* Added:
	* Note added about populating test data for v1 and v2 behave tests
    * v3 before_all and v3 after_all for behave tests
    * v3 behave tests for test-data endpoints 
* Modified:
	* README formatting has been fixed
	* v1 behave tests can use a generated analytics_id from the before_all features function in v1/environment.py
	* v1 behave tests can use a generated media_api_key from the before_all features function in v1/environment.py
    * more validation logic for valid_analytics_id and valid_media_api_key 
* Deleted:
    * results are no longer checked in the v1 pagination feature file

###### 2. What have you learned?
* It's super important to encode query parameters before making an HTTP request
* Regex matches with exact lengths will match longer strings
* Feature files are very exacting about formatting

###### 3. What inputs should be tested/might be troublesome?
* Should enumerate all possible inputs for behave test-data endpoints in v3

###### 4. Any code smells?
* Yes, v1/environment.py and v2/environment.py are basically the same code.

### [x] Manually test the code
### [x] Run the unit tests
### [x] Run the integration tests
### [-] Run the coverage tests

## Post-Review
### What did you think of the PR overall?
* Love the initiative to encourage full local development

### What would you suggest changing architecturally?
* Architecturally it's a bit odd that v1 an v2 behave tests depend on a v3 endpoint. Why not make the v3/test-data endpoint a v1? Then behave tests that are more recent depend on older version endpoints instead of future ones.

### What could more optimal in this PR?
* v1/environment.py and v2/environment.py have code duplication

### What further testing would you suggest?
* Added it inline in the comments. 

### Any other comments?
* No