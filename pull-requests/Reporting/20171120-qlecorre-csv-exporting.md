# qlecorre-csv-exporting

## Pre-Review
### What will this Pull Request do?
Add csv as a valid format to receive API responses in

### Why is this Pull Request needed?
To reach feature parity with the Segmentation API as we want Portal to use Reporting API instead

### What's the *one* goal of this PR? (cleaning/refactoring/feature/bugfix)
Feature
Refactoring
Cleaning

### Are there any points in the code the reviewer needs to double check?
Check the response object

### Are there any Pull Requests open in other repos which need to be merged with this?
No

### What issues does this address? (Please link tickets)
AN-2180

### Does the PR name match the standard?
  1. [x] Name includes ticket number
  2. [-] Name is categoried in path. For example: feature/BIG-1265

### Is the commit history squashed?
Yes. Only one commit

## Review
### [x] Pull down the code from the branch
### [x] Does it start/compile without modification?
### [-] Is it style compliant? (PEP8/Google/...)
### [] Read the code
###### 1. What parts of the code have been added/modified/deleted?
* Added:
    1. Added a check in can_handle for PG and Mongo for CSV format
    2. Added a query parameter in the call to segmentation for response format
    3. Validation of response type requested
* Modified:
    1. Conditionally formats API response depending on format requested
* Deleted:

###### 2. What have you learned?
Q's code needs to be ready carefully because he has a tendency to write too much of it

###### 3. What inputs should be tested/might be troublesome?
What if you make a request with no format?
What if you make a request with a format that isn't csv or json?

###### 4. Any code smells?
### [x] Manually test the code
* Tested with no format -> defaults to json
* Tested with format==json -> got back json
* Tested with format==csv -> got back csv
* Tested with format==tsv -> got back a validation error
### [x] Run the unit tests
```
Ran 145 tests in 10.294s

FAILED (errors=34)
```
### [x] Run the integration tests
These also seem fairly broken

### [-] Run the coverage tests

## Post-Review
### What did you think of the PR overall?
The functionality is there but there seems to be some extra code

### What would you suggest changing architecturally?
Pass the format value along and make decisions further along

### What could more optimal in this PR?
Convert case statements into static dicts which would make extending this functionality easier

### What further testing would you suggest?
Please fix the unit and integration tests :)

### [x] Manually test the code
* Tested with no format -> defaults to json
* Tested with format==json -> got back json
* Tested with format==csv -> got back csv
* Tested with format==tsv -> got back a validation error
### [x] Run the unit tests
```
Ran 145 tests in 10.294s

FAILED (errors=34)
```
### [x] Run the integration tests
These also seem fairly broken