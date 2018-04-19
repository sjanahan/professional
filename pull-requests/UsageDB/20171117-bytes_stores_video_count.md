# 20171117-bytes_stores_video_count by Sahil

## Pre-Review
### What will this Pull Request do?
* Create a schema for storing plays, ad_completes, bytes streamed, bytes stored, and media_count.

* site_id is associated with bytes_stored and media_count

* analytics_id is associated with plays, ad_completes, and bytes streamed

### Why is this Pull Request needed?
As part of the SOA initiative, we want to move this functionality into its own service.
Currently, this is in BOTR.

### What's the *one* goal of this PR? (cleaning/refactoring/feature/bugfix)
Feature

### Are there any points in the code the reviewer needs to double check?
Whether the indexes are the right ones for the use cases

### Are there any Pull Requests open in other repos which need to be merged with this?
No

### What issues does this address? (Please link tickets)
AN-2124

### Does the PR name match the standard?
  1. [x] Name includes ticket number
  2. [] Name is categoried in path. For example: feature/BIG-1265

### Is the commit history squashed?
Yes

## Review
### [x] Pull down the code from the branch
### [x] Does it start/compile without modification?
### [-] Is it style compliant? (PEP8/Google/...)
### [] Read the code
###### 1. What parts of the code have been added/modified/deleted?
* Added:
    1. A table for media_storage
    2. An index on the media_storage table by date
    3. Primary key for media_storage is (site_id, date)
* Modified:
* Deleted:

###### 2. What have you learned?
* The order of a composite key matters for an index in a relational db because prefix matching

###### 3. What inputs should be tested/might be troublesome?
* How do we represent invalid bytes_stored of media_count?

###### 4. Any code smells?
### [-] Manually test the code
### [-] Run the unit tests
### [-] Run the integration tests
### [-] Run the coverage tests

## Post-Review
### What did you think of the PR overall?
Very concise. I like it

### What would you suggest changing architecturally?
Other than handling cases of invalid metrics, nothing.

### What could more optimal in this PR?
Nothing I can see

### What further testing would you suggest?
None

### Any other comments?
* What exactly comes into the database? I'm guessing it is as batch_aggregates.

* Where does the aggregation from batch to daily take place?

* What services will be writing to this? 

* What services will be reading from it? What kind of queries will they be running?
