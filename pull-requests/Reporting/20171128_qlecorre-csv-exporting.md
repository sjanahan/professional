# 20171128-qlecorre-csv_exporting

## Pre-Review
### What will this Pull Request do?
Add csv as a valid format to receive API responses in

### Why is this Pull Request needed?
To reach feature parity with the Segmentation API as we want Portal to use Reporting API instead

### What's the *one* goal of this PR? (cleaning/refactoring/feature/bugfix)
Feature
Refactoring
Cleaning

### Are there any points in the code the reviewer needs to double check?
Check the response object

### Are there any Pull Requests open in other repos which need to be merged with this?
No

### What issues does this address? (Please link tickets)
AN-2180

### Does the PR name match the standard?
  1. [x] Name includes ticket number
  2. [-] Name is categoried in path. For example: feature/BIG-1265

### Is the commit history squashed?
No, let's learn how to :)

## Review
### [x] Pull down the code from the branch
### [x] Does it start/compile without modification?
### [-] Is it style compliant? (PEP8/Google/...)
### [] Read the code
###### 1. What parts of the code have been added/modified/deleted?
* Added:
    1. Many unit tests are analytics report
    2. Many unit tests around the response format parameter
* Modified:
    1. Added many parameters to generate_test_query
    2. The old base unit test class
* Deleted:

###### 2. What have you learned?
* We seem to have a lot of unit tests for private functions of classes which made refactoring very involved

###### 3. What inputs should be tested/might be troublesome?
* Any multitude of inputs could be troublesome. Anything relating to business logic which should be outlined somewhere

###### 4. Any code smells?
* Unit testing of private functions

### [-] Manually test the code
### [x] Run the unit tests
### [x] Run the integration tests
* Many broken tests
### [-] Run the coverage tests

## Post-Review
### What did you think of the PR overall?
Overall it gets the job done. I am a bit skeptical of unit testing of private functions

### What would you suggest changing architecturally?
If these private functions need to be unit tests, perhaps they belong as public functions on another object/utility

### What could more optimal in this PR?
There are three things being done here
1. Feature added (query validation and normalization)
2. Refactoring of various codes
3. Cleanup all around

*Ideally*, you'd choose one :)

### What further testing would you suggest?
* Are the these behave tests failing for you?
```buildoutcfg
Failing scenarios:
  ../apigw.feature:17  Account without advanced_analytics -- @1.1 dev
  ../apigw.feature:18  Account without advanced_analytics -- @1.2 dev
  ../apigw.feature:19  Account without advanced_analytics -- @1.3 dev
  ../apigw.feature:20  Account without advanced_analytics -- @1.4 dev
  ../apigw.feature:21  Account without advanced_analytics -- @1.5 dev
  ../apigw.feature:22  Account without advanced_analytics -- @1.6 dev
  ../apigw.feature:23  Account without advanced_analytics -- @1.7 dev
  ../apigw.feature:24  Account without advanced_analytics -- @1.8 dev
  ../apigw.feature:25  Account without advanced_analytics -- @1.9 dev
  ../apigw.feature:26  Account without advanced_analytics -- @1.10 dev
  ../apigw.feature:27  Account without advanced_analytics -- @1.11 dev
  ../apigw.feature:28  Account without advanced_analytics -- @1.12 dev
  ../apigw.feature:29  Account without advanced_analytics -- @1.13 dev
  ../apigw.feature:30  Account without advanced_analytics -- @1.14 dev
  ../apigw.feature:31  Account without advanced_analytics -- @1.15 dev
  ../apigw.feature:32  Account without advanced_analytics -- @1.16 dev
  ../apigw.feature:33  Account without advanced_analytics -- @1.17 dev
  ../apigw.feature:34  Account without advanced_analytics -- @1.18 dev
  ../apigw.feature:35  Account without advanced_analytics -- @1.19 dev
  ../apigw.feature:36  Account without advanced_analytics -- @1.20 dev
  ../apigw.feature:39  Account without advanced_analytics -- @2.1 stg
  ../apigw.feature:40  Account without advanced_analytics -- @2.2 stg
  ../apigw.feature:41  Account without advanced_analytics -- @2.3 stg
  ../apigw.feature:42  Account without advanced_analytics -- @2.4 stg
  ../apigw.feature:43  Account without advanced_analytics -- @2.5 stg
  ../apigw.feature:44  Account without advanced_analytics -- @2.6 stg
  ../apigw.feature:45  Account without advanced_analytics -- @2.7 stg
  ../apigw.feature:46  Account without advanced_analytics -- @2.8 stg
  ../apigw.feature:47  Account without advanced_analytics -- @2.9 stg
  ../apigw.feature:48  Account without advanced_analytics -- @2.10 stg
  ../apigw.feature:49  Account without advanced_analytics -- @2.11 stg
  ../apigw.feature:50  Account without advanced_analytics -- @2.12 stg
  ../apigw.feature:51  Account without advanced_analytics -- @2.13 stg
  ../apigw.feature:52  Account without advanced_analytics -- @2.14 stg
  ../apigw.feature:53  Account without advanced_analytics -- @2.15 stg
  ../apigw.feature:54  Account without advanced_analytics -- @2.16 stg
  ../apigw.feature:55  Account without advanced_analytics -- @2.17 stg
  ../apigw.feature:56  Account without advanced_analytics -- @2.18 stg
  ../apigw.feature:57  Account without advanced_analytics -- @2.19 stg
  ../apigw.feature:58  Account without advanced_analytics -- @2.20 stg
  ../apigw.feature:61  Account without advanced_analytics -- @3.1 prd
  ../apigw.feature:62  Account without advanced_analytics -- @3.2 prd
  ../apigw.feature:63  Account without advanced_analytics -- @3.3 prd
  ../apigw.feature:64  Account without advanced_analytics -- @3.4 prd
  ../apigw.feature:65  Account without advanced_analytics -- @3.5 prd
  ../apigw.feature:66  Account without advanced_analytics -- @3.6 prd
  ../apigw.feature:67  Account without advanced_analytics -- @3.7 prd
  ../apigw.feature:68  Account without advanced_analytics -- @3.8 prd
  ../apigw.feature:69  Account without advanced_analytics -- @3.9 prd
  ../apigw.feature:70  Account without advanced_analytics -- @3.10 prd
  ../apigw.feature:71  Account without advanced_analytics -- @3.11 prd
  ../apigw.feature:72  Account without advanced_analytics -- @3.12 prd
  ../apigw.feature:73  Account without advanced_analytics -- @3.13 prd
  ../apigw.feature:74  Account without advanced_analytics -- @3.14 prd
  ../apigw.feature:75  Account without advanced_analytics -- @3.15 prd
  ../apigw.feature:76  Account without advanced_analytics -- @3.16 prd
  ../apigw.feature:77  Account without advanced_analytics -- @3.17 prd
  ../apigw.feature:93  Account with advanced_analytics -- @1.1 dev
  ../apigw.feature:94  Account with advanced_analytics -- @1.2 dev
  ../apigw.feature:95  Account with advanced_analytics -- @1.3 dev
  ../apigw.feature:96  Account with advanced_analytics -- @1.4 dev
  ../apigw.feature:97  Account with advanced_analytics -- @1.5 dev
  ../apigw.feature:98  Account with advanced_analytics -- @1.6 dev
  ../apigw.feature:99  Account with advanced_analytics -- @1.7 dev
  ../apigw.feature:100  Account with advanced_analytics -- @1.8 dev
  ../apigw.feature:101  Account with advanced_analytics -- @1.9 dev
  ../apigw.feature:102  Account with advanced_analytics -- @1.10 dev
  ../apigw.feature:103  Account with advanced_analytics -- @1.11 dev
  ../apigw.feature:104  Account with advanced_analytics -- @1.12 dev
  ../apigw.feature:105  Account with advanced_analytics -- @1.13 dev
  ../apigw.feature:106  Account with advanced_analytics -- @1.14 dev
  ../apigw.feature:107  Account with advanced_analytics -- @1.15 dev
  ../apigw.feature:108  Account with advanced_analytics -- @1.16 dev
  ../apigw.feature:109  Account with advanced_analytics -- @1.17 dev
  ../apigw.feature:110  Account with advanced_analytics -- @1.18 dev
  ../apigw.feature:111  Account with advanced_analytics -- @1.19 dev
  ../apigw.feature:112  Account with advanced_analytics -- @1.20 dev
  ../apigw.feature:115  Account with advanced_analytics -- @2.1 stg
  ../apigw.feature:116  Account with advanced_analytics -- @2.2 stg
  ../apigw.feature:117  Account with advanced_analytics -- @2.3 stg
  ../apigw.feature:118  Account with advanced_analytics -- @2.4 stg
  ../apigw.feature:119  Account with advanced_analytics -- @2.5 stg
  ../apigw.feature:120  Account with advanced_analytics -- @2.6 stg
  ../apigw.feature:121  Account with advanced_analytics -- @2.7 stg
  ../apigw.feature:122  Account with advanced_analytics -- @2.8 stg
  ../apigw.feature:123  Account with advanced_analytics -- @2.9 stg
  ../apigw.feature:124  Account with advanced_analytics -- @2.10 stg
  ../apigw.feature:125  Account with advanced_analytics -- @2.11 stg
  ../apigw.feature:126  Account with advanced_analytics -- @2.12 stg
  ../apigw.feature:127  Account with advanced_analytics -- @2.13 stg
  ../apigw.feature:128  Account with advanced_analytics -- @2.14 stg
  ../apigw.feature:129  Account with advanced_analytics -- @2.15 stg
  ../apigw.feature:130  Account with advanced_analytics -- @2.16 stg
  ../apigw.feature:131  Account with advanced_analytics -- @2.17 stg
  ../apigw.feature:132  Account with advanced_analytics -- @2.18 stg
  ../apigw.feature:133  Account with advanced_analytics -- @2.19 stg
  ../apigw.feature:134  Account with advanced_analytics -- @2.20 stg
  ../apigw.feature:137  Account with advanced_analytics -- @3.1 prd
  ../apigw.feature:138  Account with advanced_analytics -- @3.2 prd
  ../apigw.feature:139  Account with advanced_analytics -- @3.3 prd
  ../apigw.feature:140  Account with advanced_analytics -- @3.4 prd
  ../apigw.feature:141  Account with advanced_analytics -- @3.5 prd
  ../apigw.feature:142  Account with advanced_analytics -- @3.6 prd
  ../apigw.feature:143  Account with advanced_analytics -- @3.7 prd
  ../apigw.feature:144  Account with advanced_analytics -- @3.8 prd
  ../apigw.feature:145  Account with advanced_analytics -- @3.9 prd
  ../apigw.feature:146  Account with advanced_analytics -- @3.10 prd
  ../apigw.feature:147  Account with advanced_analytics -- @3.11 prd
  ../apigw.feature:148  Account with advanced_analytics -- @3.12 prd
  ../apigw.feature:149  Account with advanced_analytics -- @3.13 prd
  ../apigw.feature:150  Account with advanced_analytics -- @3.14 prd
  ../apigw.feature:151  Account with advanced_analytics -- @3.15 prd
  ../apigw.feature:152  Account with advanced_analytics -- @3.16 prd
  ../apigw.feature:153  Account with advanced_analytics -- @3.17 prd
  ../apigw.feature:169  Account with advanced data access -- @1.1 dev
  ../apigw.feature:172  Account with advanced data access -- @2.1 stg
  ../apigw.feature:175  Account with advanced data access -- @3.1 prd
  ../apigw.feature:189  Test the order of metrics -- @1.1 dev
  ../apigw.feature:190  Test the order of metrics -- @1.2 dev
  ../apigw.feature:193  Test the order of metrics -- @2.1 stg
  ../apigw.feature:194  Test the order of metrics -- @2.2 stg
  ../apigw.feature:197  Test the order of metrics -- @3.1 prd
  ../apigw.feature:198  Test the order of metrics -- @3.2 prd
  ../apigw.feature:212  Test that unnecessary metric fields cause failure -- @1.1 dev
  ../apigw.feature:213  Test that unnecessary metric fields cause failure -- @1.2 dev
  ../apigw.feature:216  Test that unnecessary metric fields cause failure -- @2.1 stg
  ../apigw.feature:217  Test that unnecessary metric fields cause failure -- @2.2 stg
  ../apigw.feature:220  Test that unnecessary metric fields cause failure -- @3.1 prd
  ../apigw.feature:221  Test that unnecessary metric fields cause failure -- @3.2 prd
  ../apigw.feature:238  Test querying all dimensions eligible for compounding -- @1.1 dev
  ../apigw.feature:239  Test querying all dimensions eligible for compounding -- @1.2 dev
  ../apigw.feature:240  Test querying all dimensions eligible for compounding -- @1.3 dev
  ../apigw.feature:241  Test querying all dimensions eligible for compounding -- @1.4 dev
  ../apigw.feature:242  Test querying all dimensions eligible for compounding -- @1.5 dev
  ../apigw.feature:243  Test querying all dimensions eligible for compounding -- @1.6 dev
  ../apigw.feature:244  Test querying all dimensions eligible for compounding -- @1.7 dev
  ../apigw.feature:245  Test querying all dimensions eligible for compounding -- @1.8 dev
  ../apigw.feature:246  Test querying all dimensions eligible for compounding -- @1.9 dev
  ../apigw.feature:247  Test querying all dimensions eligible for compounding -- @1.10 dev
  ../apigw.feature:248  Test querying all dimensions eligible for compounding -- @1.11 dev
  ../apigw.feature:249  Test querying all dimensions eligible for compounding -- @1.12 dev
  ../apigw.feature:252  Test querying all dimensions eligible for compounding -- @2.1 stg
  ../apigw.feature:253  Test querying all dimensions eligible for compounding -- @2.2 stg
  ../apigw.feature:254  Test querying all dimensions eligible for compounding -- @2.3 stg
  ../apigw.feature:255  Test querying all dimensions eligible for compounding -- @2.4 stg
  ../apigw.feature:256  Test querying all dimensions eligible for compounding -- @2.5 stg
  ../apigw.feature:257  Test querying all dimensions eligible for compounding -- @2.6 stg
  ../apigw.feature:258  Test querying all dimensions eligible for compounding -- @2.7 stg
  ../apigw.feature:259  Test querying all dimensions eligible for compounding -- @2.8 stg
  ../apigw.feature:260  Test querying all dimensions eligible for compounding -- @2.9 stg
  ../apigw.feature:261  Test querying all dimensions eligible for compounding -- @2.10 stg
  ../apigw.feature:262  Test querying all dimensions eligible for compounding -- @2.11 stg
  ../apigw.feature:263  Test querying all dimensions eligible for compounding -- @2.12 stg
  ../apigw.feature:266  Test querying all dimensions eligible for compounding -- @3.1 prd
  ../apigw.feature:267  Test querying all dimensions eligible for compounding -- @3.2 prd
  ../apigw.feature:268  Test querying all dimensions eligible for compounding -- @3.3 prd
  ../apigw.feature:269  Test querying all dimensions eligible for compounding -- @3.4 prd
  ../apigw.feature:270  Test querying all dimensions eligible for compounding -- @3.5 prd
  ../apigw.feature:271  Test querying all dimensions eligible for compounding -- @3.6 prd
  ../apigw.feature:272  Test querying all dimensions eligible for compounding -- @3.7 prd
  ../apigw.feature:273  Test querying all dimensions eligible for compounding -- @3.8 prd
  ../apigw.feature:274  Test querying all dimensions eligible for compounding -- @3.9 prd
  ../apigw.feature:275  Test querying all dimensions eligible for compounding -- @3.10 prd
  ../apigw.feature:276  Test querying all dimensions eligible for compounding -- @3.11 prd
  ../apigw.feature:277  Test querying all dimensions eligible for compounding -- @3.12 prd
  ../apigw.feature:292  Test advanced analytics_report request -- @1.1 dev
  ../apigw.feature:293  Test advanced analytics_report request -- @1.2 dev
  ../apigw.feature:294  Test advanced analytics_report request -- @1.3 dev
  ../apigw.feature:297  Test advanced analytics_report request -- @2.1 stg
  ../apigw.feature:298  Test advanced analytics_report request -- @2.2 stg
  ../apigw.feature:299  Test advanced analytics_report request -- @2.3 stg
  ../apigw.feature:302  Test advanced analytics_report request -- @3.1 prd
  ../apigw.feature:303  Test advanced analytics_report request -- @3.2 prd
  ../apigw.feature:304  Test advanced analytics_report request -- @3.3 prd
  ../apigw.feature:318  Test basic analytics_report request -- @1.1 dev
  ../apigw.feature:319  Test basic analytics_report request -- @1.2 dev
  ../apigw.feature:320  Test basic analytics_report request -- @1.3 dev
  ../apigw.feature:321  Test basic analytics_report request -- @1.4 dev
  ../apigw.feature:322  Test basic analytics_report request -- @1.5 dev
  ../apigw.feature:325  Test basic analytics_report request -- @2.1 stg
  ../apigw.feature:326  Test basic analytics_report request -- @2.2 stg
  ../apigw.feature:327  Test basic analytics_report request -- @2.3 stg
  ../apigw.feature:328  Test basic analytics_report request -- @2.4 stg
  ../apigw.feature:329  Test basic analytics_report request -- @2.5 stg
  ../apigw.feature:332  Test basic analytics_report request -- @3.1 prd
  ../apigw.feature:333  Test basic analytics_report request -- @3.2 prd
  ../apigw.feature:334  Test basic analytics_report request -- @3.3 prd
  ../apigw.feature:335  Test basic analytics_report request -- @3.4 prd
  ../apigw.feature:336  Test basic analytics_report request -- @3.5 prd
  ../v2/engagement.feature:22  Test v2 engagement endpoint with data -- @1.1
  ../v2/engagement.feature:37  Test v2 engagement endpoint for different time frames -- @1.1
  ../v2/engagement.feature:38  Test v2 engagement endpoint for different time frames -- @1.2
  ../v2/engagement.feature:39  Test v2 engagement endpoint for different time frames -- @1.3
```
* Unit tests are passing! 

### Any other comments?
Let's squash your branch into one commit before we merge!