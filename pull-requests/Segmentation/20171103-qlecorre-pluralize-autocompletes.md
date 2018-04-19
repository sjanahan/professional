# 20171103_qlecorre-pluralize-autocompletes

## Pre-review

###What will this Pull Request do?
    * This pull request adds v2 endpoints for autocompletes
    * Changes the nouns that get autocompleted from singular to plural

###Why is this Pull Request needed?
    * Currently, the dashboard queries segmentation directly via a proxy service, bypassing the API gateway. This is undesirable as it forces us to maintain two outward facing APIs. We want these proxy endpoints to go through the API gateway, and as such, we need our endpoints to match the RFC that the Portal team produced.
        Link to RFC: (link)

###Are there any points in the code the reviewer needs to double check?
    * The elastic search fetch
    * That these new endpoints have feature parity with the v1 endpoints

###Are there any Pull Requests open in other repos which need to be merged with this?
    * Yes, there is one in the reporting api (link) as well as the api gateway (link). This one would go first, followed be reporting, followed by the api gateway

###What issues does this address? (Please link tickets)
    * AN-???? (link)

## Review
[x] Pull down the code from the branch?
[x] Run the code
[x] Read the code
    [x] What parts of the code have been added/modified?
        - Added:
            + An endpoint for each type of autocomplete
            + Metadata definition files and a schema definitions for all autocomplete endpoints
            + A file to query from:
                * Dict
                * Trie
                * Snowflake
                * Elasticsearch
        - Modified:
            + The create_app function to add these new autocomplete endpoints
    [x] Write down your learnings here:
        - os.sep is a platform agnostic way to get the separator used for file paths
        - importlib is a package with two purposes
            + provide the implementation of import in Python source code
            + the components to implement `import` are exposed in this package, making it easy for users to create their own custom objects (known generically as an `importer`)
        - callable defines whether an object has a __call__ function defined
        - for videos, playlist, and players (by Ryan's request)
            - exact match for id in elasticsearch
            - prefix match for display in elasticsearch
            - elastic search is only indexed for ascii letters
[x] Run the code
[x] Does it run without modification?
[x] What inputs should be tested?
    - Empty string
    - Null
    - With/without analytics
    - Case sensitive
    - Lists
    - Does it match the v1 functionality?
    - How is unicode text searches handled?
    
## Post-Review
### What did you think of the PR overall? 
    Overall I like how small the endpoint files are. I also like how the endpoints are generated dynamically from the files in the directory.

    There are handful of places where you seem to use magic numbers without comments and if you clarified those, it would be helpful to readers of the code.

### What would you suggest changing architecturally?
    I would encourage you to enumerate the kinds of input we could expect and what the expected outputs would be. 

### What further testing would you suggest?
    We don't seem to have any tests around elastic search. We have some for the other three data sources so that might be helpful for coverage sake.

    Maybe some the utility functions inside the child classes of the autocomplete base class. I wonder how long that would take and how much confidence that would give us about refactoring.

## Any other comments?
    * What JIRA tickets does this PR address?
    * What is the link to the RFC which details the query format?
    * What assumptions are present in this implementation that may not be obvious?





    

