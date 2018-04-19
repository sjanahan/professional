# 20180228-qlecorre-update-segmentation-log-loader 

## Pre-Review
### What will this Pull Request do?
Refactor the segmentation request and dimension logs into the new framework

### Why is this Pull Request needed?
To standardize how jobs in the repository are structured

### What's the *one* goal of this PR? (cleaning/refactoring/feature/bugfix)
Refactoring

### Are there any points in the code the reviewer needs to double check?
Utils

### Are there any Pull Requests open in other repos which need to be merged with this?
No

### What issues does this address? (Please link tickets)
Free-Play initiative to get teams to write their own ETL jobs

### Does the PR name match the standard?
  1. [-] Name includes ticket number
  2. [-] Name is categorized in path. For example: feature/BIG-1265

### Is the commit history squashed?
No

## Review
### [x] Pull down the code from the branch
### [-] Does it start/compile without modification?
### [-] Is it style compliant? (PEP8/Google/...)
### [x] Read the code
###### 1. What parts of the code have been added/modified/deleted?
* Added:
    1. load file
    2. ddl definitions for necessary tables 
    3. args file per job now
* Modified:
    1. s3 utils expanded
* Deleted:
    1. deleted the old loader script

###### 2. What have you learned?
* Each job gets it's own args file in a parallel directory structure
* Solidfies the idea of returning a pair from a function

###### 3. What inputs should be tested/might be troublesome?
* We'll find out in Dev b/c we don't have functional tests or scalability tests

###### 4. Any code smells?
### [-] Manually test the code
### [-] Run the unit tests
### [-] Run the integration tests
### [-] Run the coverage tests

## Post-Review
### What did you think of the PR overall?
Loved it. Very easy to read from higher levels. Great comments about WHY. Someone understands this repo and the jobs within it.

### What would you suggest changing architecturally?
Nothing

### What could more optimal in this PR?
Nothing

### What further testing would you suggest?
None

### Any other comments?
All good. Looks great. Just the inline comments
