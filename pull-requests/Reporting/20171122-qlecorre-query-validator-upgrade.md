# 20171122-qlecorre-query-validator-upgrade

## Pre-Review
### What will this Pull Request do?
Move query validation logic from segmentation to reporting API

### Why is this Pull Request needed?
Because we want the dashboard to query Reporting API instead of using the proxy to hit segmentation

### What's the *one* goal of this PR? (cleaning/refactoring/feature/bugfix)
Refactoring

### Are there any points in the code the reviewer needs to double check?
Focus on how the files are split
Does the refactor make sense?

### Are there any Pull Requests open in other repos which need to be merged with this?
No

### What issues does this address? (Please link tickets)
AN-2146

### Does the PR name match the standard?
  1. [x] Name includes ticket number
  2. [-] Name is categoried in path. For example: feature/BIG-1265

### Is the commit history squashed?
Nope

## Review
### [x] Pull down the code from the branch
### [x] Does it start/compile without modification?
### [-] Is it style compliant? (PEP8/Google/...)
### [] Read the code
###### 1. What parts of the code have been added/modified/deleted?
* Added:
    1. A file for cities enums
    2. A file for countries enums
    3. A file for sdk_platform enums
    4. A file for video_durations enums
    5. A utility for loading the files above
* Modified:
    1. The name of query_validator class as well as the function names 
* Deleted:
    * None

###### 2. What have you learned?
* There's a lot of code responsible for validating and formatting of dimensions

###### 3. What inputs should be tested/might be troublesome?
* Different invalid formats - Do we have any gotchas from the past?

###### 4. Any code smells?
* Yes, there seems to be a good amount of code duplication in the util to load enums from file
* Yes, there are too many parameters being passed to some of those functions - might be time for classes

### [-] Manually test the code
### [x] Run the unit tests
### [-] Run the integration tests
### [-] Run the coverage tests

## Post-Review
### What did you think of the PR overall?
There's seemingly a good amount of code duplication

### What would you suggest changing architecturally?
Nothing comes to mind. I really like breaking out the lookups into different files. I like the generic loading into memory. 

### What could more optimal in this PR?
Maybe creating some classes/dicts for functions that are taking 4 or 5 parameters.
Generalizing some of those functions too

### What further testing would you suggest?
Do we need to add some more comprehensive behave testing for all the validation code?
Maybe unit tests would be good for those as well.

### Any other comments?
Nope
