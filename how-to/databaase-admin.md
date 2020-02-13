Snowflake Management

Table of Contents

Users
Define Users
Best practices for users
Roles
Define Roles
Best practices for Roles
Automation of Role grants
Databases
Define Databases
Best practices for Databases
Warehouses
Define Warehouses
Best practices for warehouses

#Quick Links
SQL to create user
SQL to create db
#### 1. Users
##### 1a. Define Snowflake Users
* Each Engineer can be a user (MFA)
* Each Product Manager can be a user (MFA)
* Applications (non-MFA)
* Segmentation
* Feeds
* Kettle "old"
* Snowflake-Loader
* External Services (non-MFA)
* ModeAnalytics
* Looker
* Stitch
* Development users (non-MFA enabled - one per team)
##### 1b. Best Practices for Users
* Users have default warehouse DEVELOPMENT
* Users have default role
* ENGINEER for engineers
* PRODUCT_MANAGER for pms
* SCRATCH_ACCESS_ONLY
* Users may be deactivated if inactive for 1 month
##### Applications standards:
* Applications will have one User and will not share it
* Applications should own a different user with different credentials for different environments
* Application passwords are stored in SALT and kept private
* Application users are versioned in github, and aligned to LDAP entitlement groups

#### 2. Roles
##### 2a. Define Snowflake Roles
* ACCOUNTADMIN - Devops
* SYSADMIN  - Team leads and Devops
* ENGINEER - All engineers
* PRODUCT_MANAGER - Anyone who wants it
##### Per Team Roles
* Have all access to developer_and_scientist_sandbox.<TEAM-NAME>.*
##### Per Service Roles
1. SERVICE_ADMIN
1. SERVICE_READ_DEV
1. SERVICE_READ_STG
1. SERVICE_READ_PRD
1. SERVICE_WRITE_DEV
1. SERVICE_WRITE_STG
1. SERVICE_WRITE_PRD
1. PUBLIC
1. SECURITYADMIN
1. READONLY - we don't want a universal readonly for privacy concerns
1. AWS_USER
1. CREATE_TABLE_PING_DATA
1. DEV_USER, STG_USER, PRD_USER
1. ANALYTICS_WRITER, ANALYTICS_READER
##### 2b. Best Practices for Roles
* Engineers will be granted all non-write Services roles, for applications in their purview
* External applications (Mode, Looker, etc...) will only be granted PRODUCT_MANAGER credentials
###### ACCOUNTADMIN:
* resetting passwords 
* creating/deleting users
###### SYSADMIN:
* Reviewing billing or historical queries
* Creating new services/roles/databases
###### ENGINEER:
* Has ADMIN privileges on all *_USER databases
###### PRODUCT_MANAGER:
* Can read from a curated set of tables + databases which match an SLA from service owners
* May want ability to create materialized views and refresh them
###### Roles for applications
* Naming will always follow "SERVICE_PERMISSIONS_ENV"
* PERMISSIONS is READ or WRITE
* ENV is DEV, STG or PRD
* Each application will have a single SERVICE_ADMIN role which has complete sudo power for anything in the database assigned to the service
* Engineers should only use the *_ADMIN role as part of DDL changes for releases or to backfill/re-process
###### Roles for TEAM_<NAME>_DEVELOPMENT_ROLE
* To enable developers to not have to modify code to run local code against snowflake. Forces developers to use a sandbox restricted database
##### 2c. Automation for Role Grants
* Services are defined and versioned in github, and aligned to LDAP entitlement groups
* LDAP group management is manual from Devops 
* Future plan is to allow teams to control groups
* A jenkins job can kick off a "grants" update 
* This could be automated in the future by either Polling or tailing logs
* The update 


#### 3. Databases
##### 3a. Define Databases
###### Per Service Databases
1. SEGMENTATION_DEV
1. SEGMENTATION_STG
1. SEGMENTATION_PRD
1. DISC_DEV
1. DISC_STG
1. DISC_PRD
1. BI_DEV
1. BI_STG
1. BI_PRD
1. AWS_USAGE_DATA
###### Per User Databases
1. USER_SAHIL
1. USER_DONATO
1. USER_XYZ
1. TMP
1. TEST_ANALYTICS
1. DATA_SESSIONS_TEST
1. TMP_ANALYTICS
1. SAHIL_TEST_ANALYTICS
1. PING_DATA, DEV_PING_DATA
1. DEV_ANALYTICS, STG_ANALYTICS, PRD_ANALYTICS
1. UTIL_DB
1. DEMO_DB

###### 3b. Best Practices for Databases
* A single database is aligned to a single service
* The owner of the database is the SERVICE_ADMIN role
* Any user may have their own database upon request, named in the format "USER_<LDAP_USERNAME>"
* User databases will give sudo access to ENGINEER role
* The TMP databases is shared and may be used for ad-hoc explorations. Tables within it MAY be deleted after 1 month from the creation time
* A new ephemeral database can be created using the suffix "_TMP" in which case it MAY be deleted after 1 month from the creation time
* Swap tables will be named the same as the original table, but suffixed with "_TMP"
* Tables within the Database will be tracked here Database tracker
* Relational tables will follow these naming conventions

#### 4. Warehouses
#### Define Warehouses
1. Development 
1. DEVELOPMENT (S)
1. BACKFILL_BRIGADE (S-L)
1. LOAD_TEST (S-L)
1. Ad-Hoc Exploration
1. AD_HOC_BASIC (shared)
1. AD_HOC_LARGE
1. Business Intelligence (Looker + Mode)
1. AD_HOC_BASIC (shared)
1. AD_HOC_NO_TIMEOUTS
1. Segmentation
1. PRD_SEGMENTATION_API -> power the api
1. PRD_SEGMENATION_LOADER -> daily load of all_ping data
1. SHARED_TINY_TASKS (shared) -> poller, load play sessions
1. Feeds
1. SHARED_TINY_TASKS (shared) -> load feed data

4b. Best Practices  for Warehouses
* Applications in the Local/Dev/Stg environments should use the DEVELOPMENT warehouse
* Warehouses should be created when there is a desire to separate out billing requirements per service or use-case


Appendix

```
CREATE USER terence
PASSWORD = 'changeme' MUST_CHANGE_PASSWORD = TRUE
LOGIN_NAME = 'terence'
DISPLAY_NAME = 'terence'
FIRST_NAME = 'Terence'
LAST_NAME = 'Hegarty'
EMAIL = 'terence@jwplayer.com'

-- Defaults
DEFAULT_ROLE = "ENGINEER"
DEFAULT_WAREHOUSE = 'DEVELOPMENT';

-- Grants
GRANT ROLE "READONLY" TO USER terence;
GRANT ROLE "PRODUCT_MANAGER" TO USER terence;
GRANT ROLE "ENGINEER" TO USER terence;


/* -----------------------------------------
 * Create a user database for personal dev *
 * --------------------------------------- */
USE WAREHOUSE DEVELOPMENT;
USE ROLE SYSADMIN;

CREATE DATABASE USER_DONATO;

GRANT OWNERSHIP ON DATABASE
USER_DONATO
TO ENGINEER;

GRANT OWNERSHIP ON SCHEMA
USER_DONATO.PUBLIC
TO ENGINEER;

-- VERIFY
USE ROLE ENGINEER;
CREATE TABLE USER_DONATO.PUBLIC.abc (C1 STRING);
DROP TABLE USER_DONATO.PUBLIC.abc;

/* -----------------------------------------
 * Create a database for new service       *
 * --------------------------------------- */


```


