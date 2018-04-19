# 20171205-qlecorre-list-fields-v5

## Pre-Review
### What will this Pull Request do?
* Add a new endpoint to surface the dimensions, metrics, and filters as well as their categorical grouping for presentation in the segmentation product

### Why is this Pull Request needed?
* To revamp the segmentation product

### What's the *one* goal of this PR? (cleaning/refactoring/feature/bugfix)
Feature

### Are there any points in the code the reviewer needs to double check?
Not sure

### Are there any Pull Requests open in other repos which need to be merged with this?
Yes, qlecorre-list-fields-v5-enfore-rec-for-pin 

### What issues does this address? (Please link tickets)
AN-2165

### Does the PR name match the standard?
  1. [X] Name includes ticket number
  2. [-] Name is categoried in path. For example: feature/BIG-1265

### Is the commit history squashed?
Yes

## Review
### [X] Pull down the code from the branch
### [X] Does it start/compile without modification?
### [-] Is it style compliant? (PEP8/Google/...)
### [X] Read the code
###### 1. What parts of the code have been added/modified/deleted?
* Added:
    1. Add a list_fields endpoint to the flask app
    2. Adds tests for checking for entitlements
    3. Adds tests for listing fields v5
        1. Making sure v5 dimensions/metrics includes v4
    4. Adds a resource for list of fields available
* Modified:
    1. Redefined dimensions and metrics
* Deleted:

###### 2. What have you learned?
* `Recommendations` are an entitlement reporting api must be aware of
* If you're going to use analogies in test files, make sure they're coherent

###### 3. What inputs should be tested/might be troublesome?
What if the site_id provided is not 8 digit alphanumeric?

###### 4. Any code smells?
### [x] Manually test the code
1. Ran it with a legitimate site_id -> works
2. Ran it with a site_id that was too short -> works but shouldn't
3. Ran it with a site_id that was too long -> works but shouldn't
4. Ran it with a site id that wasn't alphanumeric -> work's but shouldn't 
### [x] Run the unit tests
### [] Run the integration tests
### [-] Run the coverage tests

## Post-Review
### What did you think of the PR overall?
I like the PR overall.
Things I like:
1. The comments are much more about why than what
2. The functions themselves are small and with one responsibility
3. That you limited the scope of this PR to definitions and unit tests!

Things I didn't like:
1. The analogies in the test files were not thorough. Made it hard to follow the logic

### What would you suggest changing architecturally?


### What could more optimal in this PR?
The analogies in the test files

### What further testing would you suggest?
* Can we validate that the site_id is eight digit with a limited character set? Right now I can put anything non-null and it works
* I ran the following inputs manually and three of them acting differently than I expected:
1. Ran it with a legitimate site_id -> works
2. Ran it with a site_id that was less than 8 characters -> works but shouldn't
3. Ran it with a site_id that was more than 8 characters -> works but shouldn't
4. Ran it with a site id that wasn't alphanumeric -> works but __MAYBE__ shouldn't 
### Any other comments?
* Is this endpoint intended to be be used by API consumers? 
    * If not
        1. Why is it in the reporting api?
        2. Seems like segmentation API might be a better fit 
    * If so
        1. Great job!
* Other than 8 characters, what are the official constraints of a site_id?