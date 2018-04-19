# 20171109-feature/gen-data by Donato

## Pre-Review
### What will this Pull Request do?
Add a couple of endpoints the usage api.
1. An endpoint to create data in the database(with optional analytics_id and media_id)
2. An endpoint to delete the data that was created in step 1.

### Why is this Pull Request needed?
This PR is needed so that other teams (like Portal) can include
Usage API in their integration testing.

### Are there any points in the code the reviewer needs to double check?
Should manually test the endpoints

### Are there any Pull Requests open in other repos which need to be merged with this?
No

### What issues does this address? (Please link tickets)
AN-2107

## Review
### [x] Pull down the code from the branch
### [x] Does it start/compile without modification?
It does from scratch, but if you have a previous docker container, it must be rebuilt.
### [x] Read the code
###### 1. What parts of the code have been added/modified/deleted?
* Added:
    1. Many SQL files that will execute against the usagedb
* Modified:
* Deleted:
    1. Extraneous assignment of api

###### 2. What have you learned?
* It seems like a common theme where each endpoint is a class with a GET/POST/... method

###### 3. What inputs should be tested/might be troublesome?
* Invalid analytics_id
* Invalid media_id

###### 4. Any code smells?
* Nope
### [x] Manually test the code
* PUT endpoint
    1. analytics_id=None and media_id=None
       200 as expected
    2. analytics_id=dafdsfds and media_id=fdsfdsfdsfdsfs
       500, expected 400
    3. analytics_id=dafdsfds and media_id=fdsfdsf
       200, as expected
    4. analytics_id=dafdsfds and media_id=None
       200, as expected
    5. analytics_id=None and media_id=fdsfdsaf
       200, as expected
    6. Duplicate key error works for media_id
    7. Duplicate key error works for analytics_id
    8. Valid inputs work as well
* DELETE endpoint
### [x] Run the unit tests
* They pass with one warning
```buildoutcfg
/Users/janahan/git/analytics-api-usage/non_media/tests/db_chooser_tests.py:20: DeprecationWarning: Please use assertEqual instead.
  self.assertEquals(max_hist_date, date(2017,2,1))
```
### [x] Run the integration tests
They run and about half of the automated ones fail
### [x] Run the coverage tests
* It's not a show stopper. We would like to have this number
in jenkins so we can track it over time based on deploys

## Post-Review
### What did you think of the PR overall?
* Big improvement. Good attention to detail

### What would you suggest changing architecturally?
* Nothing

### What could more optimal in this PR?
* I really like the single responsibility of the classes

### What further testing would you suggest?
* Could add behave tests for these new endpoints

### Any other comments?
* No






