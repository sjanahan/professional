## Situation
* Gave Ernesto the rate limiting problem
* He had not worked with an API with rate limiting
* Took about 5-6 minutes for him to understand what rate limiting is
* I gave him the prompt below to demonstrate it
```
   Ernesto needs to make 240 requests to activate the modems that have been paid for but not yet  
   activated.
   Rate Limit: 60 req/min
   How many minutes will this take? 4 minutes
   GET incognito.com/provider/<provider_id>/activate/<activate_id>
    
   Prompt
       Given one API key, design a way to retrieve information from a service that employs rate limiting

    Assumptions
        You want to get the information as quickly as possible
        There will be other people at your company using this same API key
        You do not want to exceed the rate limit
```
## Ernesto's solution
* Most of what is written here is actually by me
* He was a slow typer and didn't speak much so it was difficult to understand what his solution would be
* He came up with the Request class and the Container class
* To poke holes in his interfaces, I provided IdsToActivate class and a main function
* He had a hard time writing any codes - preferred to write in comments
* At the end, he alluded to using Spring Framework constructs which instantiate objects with explicit construction
* Below is what he and I wrote together
```
public class Request {
    private String name; // customer's name
    private TimeStamp time; // when the request was made
}

//spring singleton
public class Container{
    private int maxRequest, int seconds;
    public Container(int maxRequest, int seconds)
    
    private List<Request> requests; // all of the requests ever made

    public void addRequest(Request Requestr); request);// adds  a request to the List requests    
    public void verify(); // checking list and removing items
    public bool requestAvailable(); // verify if we still have available requests
    
}

// GET incognito.com/provider/<provider_id>/activate/<activate_id>
public class IdsToActivate{
    private String providerId; // verizon, cox, spectrum
    private String activateId; // 13452, 12342, ...
}

public static void main() {
   List <IdsToActivate> ids; // read in and constructed from a text file
   // [{providerId: 'verizon', activateId: '13452'}, ...]
   
   
   /*
   for (IdsToActivate pair: ids){ // each time a customer is doing a request 
       
       Request r = new Request( , Time.now());
       c.addRequest(r) // create object request and store in list
   }
   */


    class Test1 {
        inject
        container c;
        public void perform(){
            //perform 1 request  call incognito
            Request r = new Request( , Time.now());
            c.
        }
    }
}
```

### Questions he had for me:
* Multiple projects or one at a time?
* Java and python programs? Yes
* Do you work on weekends?
* What hours do you keep?

### Questions I had for him
* Where do you work now?
  * Fox Home Entertainment 20th Century
* What was a recent project you worked on?
  * Elasticsearch worked on the POC
  * The project has been approved
  * Migrating an Oracle DB to Elasticsearch
  * Titles of movies in Elasticsearch
  * Title -> {Metadata about the Title}
  * Cobio from Salesforce
* What's the advantage of using Elasticsearch?
  * Faster aggregations
* Do you know why Elasticsearch is faster?
  * Lucene that Elasticsearch
  * Flattened value pairs storage
  * He is more focused on the queries
  * When I asked him to give me examples of queries he wrote against ElasticSearch, this is what he provided:
```
{
        "query" : {
            "match" : {
                "titleName" : "lion"
            }
        }
    
    }
    
    {
        metadata
        source: {
            {
            }
            {
            }
        }
    
    }
```
