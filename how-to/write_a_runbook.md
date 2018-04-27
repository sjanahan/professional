# <Service Name> Runbook
Owned by <*Team Name*> Team
## Monitors

1. If a link is used more than once, make it a reference link at the top of this document and reference it in the body of this document to reduce redundancy.
1. When adding a runbook for a new datadog alert, be sure to follow the below template:
    ```markdown
    ### Datadog Monitor Name
    1. What does this alert mean?
        - One sentence description
    2. What is the urgency of this alert?
        - Critical/high/medium/lowest
    3. How quickly does this alert need to be dealt with?
        - 1 hour/4 business hours/1 business day
    4. What is the impact of this alert going off?
        - In terms of money, SLAs, impact to other teams
    ##### Troubleshooting
    1. Step:
        - Instructions
        - If possible outcome of step:
            - Instructions
            - [link to next step][reference link]
        - Else if possible outcome of step:
            - Instructions
            - [link to next step][reference link]
        - Else:
            - Instructions
            - [link to next step][reference link]

    2. Step:
        - etc.
    ```
