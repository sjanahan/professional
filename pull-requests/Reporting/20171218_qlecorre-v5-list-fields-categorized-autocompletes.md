# 20171218_qlecorre-v5-list-fields-categorized-autocompletes 

## Pre-Review
### What will this Pull Request do?
Groups the filters into the same categories as dimensions

### Why is this Pull Request needed?
Necessary for the grouping in the UI as per the mock

### What's the *one* goal of this PR? (cleaning/refactoring/feature/bugfix)
Cleaning to the spec

### Are there any points in the code the reviewer needs to double check?
No

### Are there any Pull Requests open in other repos which need to be merged with this?
No

### What issues does this address? (Please link tickets)
AN-2229

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
  1. Added new tests for the list_fields endpoint
* Modified:
  1. Added a section to the analytics request contract about how filters should be formatted
  2. Refactored the list class in v5 to be more generic
* Deleted:
###### 2. What have you learned?
* Filters shared their categories with dimensions, not metrics

###### 3. What inputs should be tested/might be troublesome?
* Why are invalid site_ids accepted as a query parameter?

###### 4. Any code smells?
### [-] Manually test the code
### [x] Run the unit tests
* After merging in develop, [10 tests fail](https://gist.github.com/sjanahan/7232c08adcb5e9eb687eeaf39d553d22)

### [x] Run the integration tests
```
*Failing scenarios:
  v4/request-validation.feature:33  Test analytics_report request -- @1.16 requests
```
### [x] Run the coverage tests

## Post-Review
### What did you think of the PR overall?
It's okay. The PR was not up to date with develop

### What would you suggest changing architecturally?
Nothing

### What could more optimal in this PR?
Fix the unit and behave tests

### What further testing would you suggest?
Fix the existing tests and ask yourself if they still make sense

#### [x] Run the unit tests
* After merging in develop, [10 tests fail](https://gist.github.com/sjanahan/7232c08adcb5e9eb687eeaf39d553d22)

#### [x] Run the integration tests
```
*Failing scenarios:
  v4/request-validation.feature:33  Test analytics_report request -- @1.16 requests
```
### Any other comments?
No
