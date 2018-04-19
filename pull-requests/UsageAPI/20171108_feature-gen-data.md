# 20171108_feature/gen-data by Donato

## Pre-Review
### What will this Pull Request do?
Adds two endpoints to usage api
1. A PUT endpoint so testers can generate data (optionally: choose what data is created)
2. A DELETE endpoint so testers can clean up what they generated
### Why is this Pull Request needed?
So that other teams can use the usage api in their integration testing
### Are there any points in the code the reviewer needs to double check?
* Anything that connects to a database
* The data being inputted
### Are there any Pull Requests open in other repos which need to be merged with this?
No
### What issues does this address? (Please link tickets)
AN-2107

## Review
### [x] Pull down the code from the branch
### [x] Run the code
### [x] Does it run without modification?
### [x] Read the code
###### 1. What parts of the code have been added/modified/deleted?
* Added:
    1. Two endpoints
* Modified:
    1. Just the index page
* Deleted:
    1. None
###### 2. What have you learned?
* Analytics_id must be a valid uuid
* Connect_timeout for psycopg2 lib is in seconds
* Statement_timeout for psycopg2 lib is in milliseconds
###### 3. What inputs should be tested/might be troublesome?
* An analytics_id that isn't a valid uuid.
* A media_id of the wrong length
###### 4. Any code smells?
No

## Post-Review
### What did you think of the PR overall?
Good overall. Just a few comments
### What would you suggest changing architecturally?
No, I like the structure of it
### What further testing would you suggest?
None
### Any other comments?
Do you know why when launching docker-compose up for the usage db, the first few times it tries it fails?


