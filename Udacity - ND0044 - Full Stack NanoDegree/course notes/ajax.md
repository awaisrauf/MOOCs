Ajax request is asyc request: a request that can be sent without client refreshing the page. Async requests (Ajax request) can be sent 
in one of the two ways;
- XMLHttpRequest
- Fetch (Modern)

### Using XMLHttpRequest
```javascript
# build request object
var xhttp = new XMLHttpRequest();
# get object form doc
object_name = document.getElementById("name_object").value;
# open a connection 
xhtttp.open("GET", "/todos/create?object_name="+object_name);
xhttp.send();
```
In Async, client side decide how to change view. So when state is changed, this function is used. Follwoing function will change whenever 
 there is a state chagne. 

```
xhttp.onreadystatechange = function(){
\\ 4 means server thing is completed
if (this.readyState == 4 && this.status == 200) {
  // on successful response 
  console.log(xhttp.responseText);
  }
};
```

