# 0. Prompt
Create a leaderboard for services within the data team that include the following:

|Service Name|# of Monitors|# of Monitors with Link to Runbook|# of Monitors with Template Runbooks|# of alerts in last 6 months|
|------------|-------------|----------------------------------|----------------------------------|----------------------------|
|Reporting   |50           |10                                |0                                 |200                         |
|Stretch-Indexer |50       |10                                |0                                 |200                         |
|...

# 1. Resolve Ambiguity
  1. What is a template runbook?
    * [This is a runbook template](https://jwplayer.atlassian.net/wiki/spaces/INC/pages/107315391/Runbook+Template)
  
  2. How will you categorize the monitors?
    * I will first need to look at the metadata available on the monitors and deduce from there
    * I forsee the data being incomplete and it may be necessary to talk to humans 

  3. How do you know the list of services?
    * [Index of services](https://jwplayer.atlassian.net/wiki/spaces/EN/pages/70194753/Index+of+Services)

  4. Could there be a monitor which relies on multiple services?
    * Yes, I'm not sure how I would attribute such a monitor

  5. How will you figure out how many alerts a certain monitor has produced?
    * I'm not sure if this is available via the API but I will look

  6. How can we incentivize behavior to produce better runbooks?
    * If we can create a set of titles associated with deltas in statistics per service, we can gamify this a bit
    * Perhaps we can attach breakfasts to winners
  
  7. What are some titles we could award?
    * Most covered service
    * Most improved service this month
    * Most improved service this quarter
    * Greatest reduction in alerts

# 2. Create an example (with ~7 data points)
|Service | Title | Metadata |
|---     |---    | ---      |
|DD-Stretch-Team-Business-Hours | [#7207] [PROD ] stretch-indexer: Popular Indexer is critically low | None |
|MediaIntelligence              | [#7206] [MI] High k8s memory usage on container: mep-base-worker   | None |
|Media Services Livestream      | [#7205] Livestream API Service - Backend 5xx High                  | None |
|DD-Data Team Business Hours    | [#7203] [Prod] segmentation-api database queries timing out        | None |
|DD-Data Team                   | [#0000] [Prod] VPC-ANALYTICS-BLAH-BLAH has unhealthy hosts         | None |
|DD-Data Team                   | [#0001] [Prod] There are less than 2 healthy hosts                 | None |
|DD-Data Team                   | [#0002] [Prod] Reporting API poller has died!                      | None |

# 3. Brute force a solution
```  
  main
    get all monitors
    for each monitor
      categorize each monitor into a service based on available metadata

    for monitors with unknown service, add to set of unknowns
    
  categorizing monitors
    fetch all metadata and see if you can infer

  number of alerts triggered
    get all pages and match it with monitor names
```    
# 4. Time and Space Analysis
Time: O(m+p) where m is the number of monitors and p is the number of alerts
Space: O(m) or O(p), whichever is larger

# 5. Walk through your solution. Does it make sense?
Yes. 
## Is it optimal?
If we can query pagerduty for specific monitors instead of all, p would equal m and we could reduce the runtime

# 6. Code it up


# 7. Test

---
# 8. What did I learn?

# 9. Follow up items
  * []
