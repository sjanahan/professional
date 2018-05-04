# 20180503_play_session_stats 

## Pre-Review
### What will this Pull Request do?
Load play session stats into snowflake for internal use. Play session stats is an output of the 
Usage Mini Play Session job. See schema here and transformations here.

### Why is this Pull Request needed?
Core/Dan B. want to play with the data.

### What's the one goal of this PR? (cleaning/refactoring/feature/bugfix/experiment)
New feature.

### Are there any points in the code the reviewer needs to double check?
Nope.

One thing to note, the play sessions s3 output does not have date in it. 
So I have to inject the date to populate the Snowflake column. We will make the 
change in play sessions s3 to have the date however it will be a few weeks before we can get that done.

### Are there any Pull Requests open in other repos which need to be merged with this?
Nope.

### What issues does this address? (Please link tickets)
DATA-1642

### Does the PR name match the standard?
  Description includes ticket number
  Name is categorized in path. For example: feature/BIG-1265

### Is the commit history squashed?
Yes sir.

## Review
### [x] Pull down the code from the branch
### [x] Does it start/compile without modification?
### [-] Is it style compliant? (PEP8/Google/...)
### [] Read the code
###### 1. What parts of the code have been added/modified/deleted?
* Added:
    * `play_sessions/load_stats.py`
        * 
* Modified:
* Deleted:

###### 2. What have you learned?
* Q's refactor makes it super easy to add jobs.
* We should separate SQL from Python from a directory perspective for separation of concerns

###### 3. What inputs should be tested/might be troublesome?
* Not sure - we'll find out in Dev

###### 4. Any code smells?
### [-] Manually test the code
### [-] Run the unit tests
### [-] Run the integration tests
### [-] Run the coverage tests

## Post-Review
### What did you think of the PR overall?
8/10

### What would you suggest changing architecturally?
Please move the `session_stats.py` into a directory called SQL and reference it there.

### What could more optimal in this PR?
Only file organization as far as I can tell

### What further testing would you suggest?
Keep an eye on it in dev

### Any other comments?
Nope
