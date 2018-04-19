#2017_priyanka_update_canned_reports_with_queries

## Pre-Review
### What will this Pull Request do?
* Add the query that the front end will make to reporting-api for canned reports

### Why is this Pull Request needed?
* Because right now there's no queries for canned reports

### What's the *one* goal of this PR? (cleaning/refactoring/feature/bugfix)
* Feature

### Are there any points in the code the reviewer needs to double check?
* No

### Are there any Pull Requests open in other repos which need to be merged with this?
* Nope

### What issues does this address? (Please link tickets)
* AN-2199

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
    1. date_utils file
        1. function for given day D, give me X days before it
        2. function for given day D. give start and end date of that quarter
        3. function for given day D, give me last quarter's (year, month)
        4. function for given month M and year Y, give me the last day of that month
    2. lib file for canned reports
        1. function for modifying the dict to include date ranges
        2. 
* Modified:
    1. Added the reporting-API compliant queries for the canned reports from the copy
    2. The model for the response object for canned reports
* Deleted:

###### 2. What have you learned?
* Reporting API is very specific about the POST body. Can't have extra keys
* Can implement date ranges with an enum. Slick stuff with the date logic

###### 3. What inputs should be tested/might be troublesome?
* Try taking a query from the /reports endpoint and entering it into reporting-api
```
{
  "message": "Request body contains invalid JSON Schema: Additional properties are not allowed ('filters' was unexpected). Please check the 'None' field of the request body."
}
```

###### 4. Any code smells?
### [-] Manually test the code
* Try taking a query from the /reports endpoint and entering it into reporting-api
```
{
  "message": "Request body contains invalid JSON Schema: Additional properties are not allowed ('filters' was unexpected). Please check the 'None' field of the request body."
}
```
### [x] Run the unit tests
### [x] Run the integration tests
### [-] Run the coverage tests

## Post-Review
### What did you think of the PR overall?
* I really like the code organization. Very easy to follow

### What would you suggest changing architecturally?
* Nothing

### What could more optimal in this PR?
* The request body produced by the endpoint should be more closely validated. It doesn't work against the reporting API as is

### What further testing would you suggest?
* More manual testing
* Tried taking a query from the /reports endpoint and entering it into reporting-api
```
{
  "message": "Request body contains invalid JSON Schema: Additional properties are not allowed ('filters' was unexpected). Please check the 'None' field of the request body."
}
```

### Any other comments?
* Nope