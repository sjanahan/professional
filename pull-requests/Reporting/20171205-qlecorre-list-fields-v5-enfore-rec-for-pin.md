# 20171205-qlecorre-list-fields-v5-enfore-rec-for-pin

## Pre-Review
### What will this Pull Request do?
Enforce the recommendations entitlement is necessary to access pin_id metric

### Why is this Pull Request needed?
So we can upsell people on recommendations

### What's the *one* goal of this PR? (cleaning/refactoring/feature/bugfix)
Feature

### Are there any points in the code the reviewer needs to double check?
How entitlements are enforced

### Are there any Pull Requests open in other repos which need to be merged with this?
No

### What issues does this address? (Please link tickets)
AN-2165


### Does the PR name match the standard?
  1. [-] Name includes ticket number
  2. [-] Name is categorized in path. For example: feature/BIG-1265

### Is the commit history squashed?
Yes

## Review
### [x] Pull down the code from the branch
### [x] Does it start/compile without modification?
### [-] Is it style compliant? (PEP8/Google/...)
### [] Read the code
###### 1. What parts of the code have been added/modified/deleted?
* Added:
    1. More tests for intricate combinations of entitlements on categories and metrics
    2. Enforces recommendations entitlement to access pin_set_id 
* Modified:
* Deleted:

###### 2. What have you learned?
Recommendations has its own entitlement

###### 3. What inputs should be tested/might be troublesome?
There are no inputs

###### 4. Any code smells?
No 

### [-] Manually test the code
### [x] Run the unit tests
### [x] Run the integration tests
### [-] Run the coverage tests

## Post-Review
### What did you think of the PR overall?
Good. Just a few inline questions

### What would you suggest changing architecturally?
Nothing. Seems good to me.

### What could more optimal in this PR?
Nothing. Seems good to me.

### What further testing would you suggest?
None. Looks good to me.

### Any other comments?
Nope
* Unit tests pass
* Behave tests pass
