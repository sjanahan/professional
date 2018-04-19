# qlecorre-query-validator-upgrade-with-enums 

## Pre-Review
### What will this Pull Request do?
There is another PR for adding enums. This PR uses the loaded enum and validates that the query is using known ones

### Why is this Pull Request needed?
To move the query validation code from Segmentation to reporting so we can enforce it across all data sources uniformly

### What's the *one* goal of this PR? (cleaning/refactoring/feature/bugfix)
Feature

### Are there any points in the code the reviewer needs to double check?
You could try to break it by running a few queries, taking the keys returned and filter for them (making sure that keys passed back can be used for filtering) ...

### Are there any Pull Requests open in other repos which need to be merged with this?
Yes, the enum loader

### What issues does this address? (Please link tickets)
AN-2146

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
  1. Tests for the query validator
* Modified:
  1. Changed the query validator to have a larger interface that's more granular
* Deleted:

###### 2. What have you learned?
1. The validation code is much cleaner now than it was

###### 3. What inputs should be tested/might be troublesome?
1. Refer to the double check above

###### 4. Any code smells?
### [] Manually test the code
### [x] Run the unit tests
### [-] Run the integration tests
### [-] Run the coverage tests

## Post-Review
### What did you think of the PR overall?
Application code was very easy to follow

### What would you suggest changing architecturally?
No

### What could more optimal in this PR?
Nothing

### What further testing would you suggest?
None

### Any other comments?
Nope
