# Simulated Writer side effect 
## Motivation
When we run cross service scalability tests, we are writing to production tables.

We want to ensure the cleanliness of those production tables even if the writers terminate unexpectedly.

# Proposed solutions
1. Implement a solution similar to the data snowflake loader which uses a .lock file and the fcntl library to gracefully handle unexpected process termination

2. Use a service that spins up a fresh postgres database server for load testing so we need not worry about side effects on the tables used

# Open Questions
1. What should we be optimizing for in our decision?
* Developer iteration speed

2. How often do we forsee running these kinds of scalability tests?
* If infrequently, solution 2 seems more viable assuming 10 minute database startup time
* If frequently, we might save more time if we use the production instances

3. How important is it actually to clean up our mess?
* If the site_ids and analytics_ids we generate are guaranteed to not collide with
  their legitimate counterparts, what's the harm in an amount of extra data in the tables?


