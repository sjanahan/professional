# 20180214-qlecorre-uniformizing-loading-framework 

## Pre-Review
### What will this Pull Request do?
Take care of a bunch of tech debt

### Why is this Pull Request needed?
In order to faciliate non-Analytics developers from contributing to the repo, we need to deal with some
tech debt that semantically would not make sense to a new developer

### What's the *one* goal of this PR? (cleaning/refactoring/feature/bugfix)
Refactoring

### Are there any points in the code the reviewer needs to double check?
1. utils
2. default values to python scripts

### Are there any Pull Requests open in other repos which need to be merged with this?
No

### What issues does this address? (Please link tickets)
AN-2297

### Does the PR name match the standard?
  1. [x] Name includes ticket number
  2. [-] Name is categorized in path. For example: feature/BIG-1265

### Is the commit history squashed?
No

## Review
### [x] Pull down the code from the branch
### [-] Does it start/compile without modification?
### [-] Is it style compliant? (PEP8/Google/...)
### [x] Read the code
###### 1. What parts of the code have been added/modified/deleted?
* Added:
    * new shell scripts 
* Modified:
    * utils
* Deleted:
    * botr_to_snowflake.py
    * load_autocomplete_domains.py
    * load_batch_play_sessions.py
    * load_media_tags.py
    * load_play_sessions.py
    * query_tempplates.py
    * session_queries.py
    * 

###### 2. What have you learned?
That we have two major classes of loads in snowflake. Metadata and Play Sessions

###### 3. What inputs should be tested/might be troublesome?
Since all jobs were touched, we have to be careful about how we roll this out

###### 4. Any code smells?
### [-] Manually test the code
### [-] Run the unit tests
### [-] Run the integration tests
### [-] Run the coverage tests

## Post-Review
### What did you think of the PR overall?
Loved it. Super easy to follow and great thought put into forwards and backwards compatibility

### What would you suggest changing architecturally?
Nothing

### What could more optimal in this PR?
Nothing. I like seeing the bleeding edge of this PR

### What further testing would you suggest?
We should be super thorough about verifying that the jobs succeed to completion in dev before promoting it.

### Any other comments?
1. Please squash the commit history!
