# 20171211-usage_monthly_endpoint by Sahil

## Pre-Review
### What will this Pull Request do?
* Add a monthly endpoint to expose usage data

### Why is this Pull Request needed?
* Part of the SOA initiative. This data is necessary for accurate billing

### What's the *one* goal of this PR? (cleaning/refactoring/feature/bugfix)
* Feature

### Are there any points in the code the reviewer needs to double check?
* No

### Are there any Pull Requests open in other repos which need to be merged with this?
* There is one in usage-db, but it has already been merged

### What issues does this address? (Please link tickets)
AN-2125

### Does the PR name match the standard?
  1. [-] Name includes ticket number
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
    1. Feature file for monthly endpoint
    2. Added more test data for inserting into media storage table
    3. Added an endpoint for monthly to the flask app
    4. Created a util file for shared functionality between daily and monthly
* Modified:
    1. Case statement for number of result in behave_utils for requesting endpoint in daily vs monthly
* Deleted:
    
###### 2. What have you learned?
* We turn dates into pages so we can get log(n) access time

###### 3. What inputs should be tested/might be troublesome?
* Funky date ranges

###### 4. Any code smells?
### [-] Manually test the code
### [x] Run the unit tests
### [x] Run the integration tests
### [-] Run the coverage tests

## Post-Review
### What did you think of the PR overall?
* Good. Reads well and thought the refactoring was a solid choice.

### What would you suggest changing architecturally?
*None

### What could more optimal in this PR?
* Marshal'ing the response object as it is complex

### What further testing would you suggest?
* None

### Any other comments?
* Please include the JIRA ticket (AN-2125) in the PR title or comment
* Please squash the commit history