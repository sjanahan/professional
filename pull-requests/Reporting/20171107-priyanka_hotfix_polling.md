# priyanka_hotfix_polling

## Pre-Review
### What will this Pull Request do?
	This PR aims to alleviate the symptoms of the poller thread dying in the reporting API.
### Why is this Pull Request needed?
	This is needed so we minimize the chance that a customer contacts us about inconsistent data
### Are there any points in the code the reviewer needs to double check?
	Yes. The logic that determines whether we are going to 500 about a dead poller. Should we allow some requests which are unaffected or 500 all?
### Are there any Pull Requests open in other repos which need to be merged with this?
	No
### What issues does this address? (Please link tickets)
	AN-????

## Review
### [x] Pull down the code from the branch
### [x] Run the code
### [x] Does it run without modification?
### [X] Read the code
### [X] What parts of the code have been added/modified/deleted?
		1. Added
			A global variable in the utils that keeps track of the expiry time of poller. We also update that upon successful requests to Postgres and Segmentation
		2. Modified
			Logic has been added to the can handle of Postgres and Segmentation to say if the poller is not alive, return a 500 and create a datadog event.
		3. Deleted
			* None
### [X] Write down your learnings here:
		1. time.time() returns time in unix epochs
### [X] What inputs should be tested?
		1. Can we create a function where the cache expiry is in the past to verify that this functionality works?

## Post-Review
### Would it make sense to let some queries work and some error when the poller has died? Or would we want to not service any requests from these data sources until the poller has been fixed?
Because this is temporary, it seems best to let us know as soon as possible that the poller has died and we need to redeploy. Depending on how long it takes for us to implement a permanent solution, that could make sense in a follow up. I think what's important for now is we know the poller thread is dead because we can do something to mitigate its impact on the API.

### What did you think of the PR overall?
It's simple to read and follow. It reports to us when there is an issue.

### What would you suggest changing architecturally?
Architecturally I like how little you've modified the code because this is a temporary solution.

### What further testing would you suggest?
I would suggest adding some unit testing that mocked out the return value of poller_is_working to verify that the functionality is working as intended. It's not strictly necessary.