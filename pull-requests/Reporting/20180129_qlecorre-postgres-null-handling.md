# 20180129_qlecorre-postgres-null-handling

## Pre-Review
### What will this Pull Request do?
Allow null to be a valid query value against postgres

### Why is this Pull Request needed?
To create a consistent querying interface across our set of persistances

### What's the *one* goal of this PR? (cleaning/refactoring/feature/bugfix)
Feature

### Are there any points in the code the reviewer needs to double check?
Manual/unit/behave tests

### Are there any Pull Requests open in other repos which need to be merged with this?
Yes, there are many in Segmentation w.r.t. autocomplete and pin set ids.

### What issues does this address? (Please link tickets)
AN-2266

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
  * A LOT of case statements to handle None input
  * A lot of tests around handling None
* Modified:
  * Unit tests 
* Deleted:

###### 2. What have you learned?
I just assumed we handled None well. I feel like this can be done more elegantly

###### 3. What inputs should be tested/might be troublesome?
Nones everywhere

###### 4. Any code smells?
### [x] Manually test the code
### [x] Run the unit tests
### [-] Run the integration tests
### [-] Run the coverage tests

## Post-Review
### What did you think of the PR overall?
It is easy to follow. I don't like how much case logic there is around supporting None

### What would you suggest changing architecturally?
Using some OO design principles to centralize the handling of None instead of all these case statements

### What could more optimal in this PR?
Reducing the number of places you touched to support None

### What further testing would you suggest?
One behave test is failing
```
Failing scenarios:
  v4/request-validation.feature:33  Test analytics_report request -- @1.16 requests
```

### Any other comments?
* Please squash the commit history!
