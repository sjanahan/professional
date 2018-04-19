# 20171214_qlecorre-v2-deprecation 

## Pre-Review
### What will this Pull Request do?
Deleting any code that uses mongo as a data source

### Why is this Pull Request needed?
To remove dead code from the reporting API

### What's the *one* goal of this PR? (cleaning/refactoring/feature/bugfix)
Cleaning

### Are there any points in the code the reviewer needs to double check?
* Manually tests the remaining endpoints
* See if the API runs as is

### Are there any Pull Requests open in other repos which need to be merged with this?
No

### What issues does this address? (Please link tickets)
AN-2228

### Does the PR name match the standard?
  1. [x] Name includes ticket number
  2. [-] Name is categoried in path. For example: feature/BIG-1265

### Is the commit history squashed?
No

## Review
### [x] Pull down the code from the branch
### [x] Does it start/compile without modification?
### [-] Is it style compliant? (PEP8/Google/...)
### [] Read the code
###### 1. What parts of the code have been added/modified/deleted?
* Added:
  1. 
* Modified:
  1. 
* Deleted:
  1. `ENABLE_ALL_V2_ENDPOINTS` config key
  2. `DEBUG` config key
  3. `TESTING` config key
  4. `MONGO` config keys
  5. `VIDEO_SLICES_DB` keys that were unused
  6. all the mongo imports in the `__init__.py` file
  7. all the v2 library imports in the `__init__.py` file
  8. all the v2 unit tests


###### 2. What have you learned?
1. There was a LOT of mongo related configuration

###### 3. What inputs should be tested/might be troublesome?
1. Anything to the V2 endpoints?
2. Unit tests that depend on mongo
3. 

###### 4. Any code smells?
### [] Manually test the code
### [] Run the unit tests
### [] Run the integration tests
### [] Run the coverage tests

## Post-Review
### What did you think of the PR overall?

### What would you suggest changing architecturally?

### What could more optimal in this PR?

### What further testing would you suggest?

### Any other comments?
* Please squash the commit history
* Can you do a coverage test before and after the deletion?
