# 20171109_feature/behave-local

## Pre-Review
### What will this Pull Request do?
This PR is supposed to fix the behave tests when run with a local db

### Why is this Pull Request needed?
So we can be confident that changes to the API don't break the API before merging to develop

### Are there any points in the code the reviewer needs to double check?
Whether the behave tests pass
Whether the behave tests cover the possible inputs

### Are there any Pull Requests open in other repos which need to be merged with this?
No

### What issues does this address? (Please link tickets)
AN-2107
AN-2108

### Does the PR name match the standard?
`Update Behave tests to continue working w/ clean db`

Seems descriptive enough to me. Not sure what our standard really is.

### Is the commit history squashed?
Yes


## Review
### [x] Pull down the code from the branch
### [x] Does it start/compile without modification?
### [-] Is it style compliant? (PEP8/Google/...)
### [] Read the code
###### 1. What parts of the code have been added/modified/deleted?
* Added: 
    1. You need to insert test data at the beginning of each month
    2. 
* Modified:
    1. v1 behave tests depend on the v3 create test data endpoint
    2. v2 behave tests depend on the v3 create test data endpoint
    3. Added v2 step implementations for a generated_analytics_id and a generated_media_id
* Deleted:
    1. Checks for number of results in some of the v2 tests

###### 2. What have you learned?
* Can do a before_all in behave for the entire set of tests

###### 3. What inputs should be tested/might be troublesome?
* This PR does not have any input that a user might make

###### 4. Any code smells?
* Why are v1 and v2 behave tests relying on a v3 endpoint?
### [] Manually test the code
### [x] Run the unit tests
### [x] Run the integration tests
Had to run the `psql -h localhost -p 8888 --username neo -d matrix -f behave/behave.tests.inserts.sql`
first.

I ran the tests with the following command `behave --tags @automated`

Had to run before_all and after_all from v4 to v3 endpoints 

After fixing that,
1. V1 passed

2. V2 passed
 
3. V3 tests skip
   
### [-] Run the coverage tests

## Post-Review
### What did you think of the PR overall?
I liked what was done with the before_all and after_all. 

### What would you suggest changing architecturally?
I find it odd that v1 and v2 behave tests rely on a v3 endpoint. 

Why not turn the large sql script that needs to be run at the beginning of each month into a test-data endpoint for v1 and/or v2?

### What could more optimal in this PR?
Not mixing api versions in the behave tests

### What further testing would you suggest?
Input tests for the test-data endpoints as they optionally take human input

### Any other comments?
No