## Pre-Review
### What will this Pull Request do?
* Add enums to the reporting API necessary for validating the post body of a request
### Why is this Pull Request needed?
* As we transition to moving all queries of customer data to the reporting API, it follows that we must centralize the query validation logic into one place as well
### What's the *one* goal of this PR? (cleaning/refactoring/feature/bugfix)
* feature
### Are there any points in the code the reviewer needs to double check?
* Is the formatting of the data files consistent?
### Are there any Pull Requests open in other repos which need to be merged with this?
* Yes, there is one. It ought to be merged into this one before merging to develop
### What issues does this address? (Please link tickets)
* AN-2146
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
  1. Huge files for the countries, cities, etc
  2. Generic file loaders
  3. Named getters 
* Modified:
* Deleted:

###### 2. What have you learned?
* Why would you not use just one delimiter?
###### 3. What inputs should be tested/might be troublesome?
* Invalid site_id

###### 4. Any code smells?
### [x] Manually test the code
### [x] Run the unit tests
### [] Run the integration tests
### [-] Run the coverage tests

## Post-Review
### What did you think of the PR overall?
Really good. I was a big fan of the enum file loader util file

### What would you suggest changing architecturally?
Nothing

### What could more optimal in this PR?
Why do we have two different delimiters?

### What further testing would you suggest?
Why don't we validate site_ids in the API?

### Any other comments?
* Please squash the commit history before merging :)
