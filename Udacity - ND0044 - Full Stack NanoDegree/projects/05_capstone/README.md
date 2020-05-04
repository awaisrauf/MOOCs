### FSND Capstone Project: A Simple News Website

Deploy Link: https://pure-river-17647.herokuapp.com/

### Abstract
This is capstone project for udacity's nano-degree on full stack web development. It is a simple
news website api which has a news page, all news page with pagination and has edit, delete and post 
news functions. Code also contains thorough test, configuration and authentciation files. 


### Project Dependencies and Local hosting
Install dependencies
```pip install -r requirements```
set environment variable `set FLASK_APP=app` and then use `flask run` command 
and head to https://127.0.0.1:5000 to see it. 

### Authentication 
App has two different rules of `writer` who has permissions of `edit:news` and `post:news` and `editor` who has two 
all the permissions including `delete:news`

### API End Points 

#### 1. GET /all_news
fetches all the news in paginated fashion. 

```json
{
  "news": [
    {
      "category": 1, 
      "description": "a", 
      "headline": "a", 
      "id": 1, 
      "img_url": "a"
    }, 
    {
      "category": 1, 
      "description": "a", 
      "headline": "a", 
      "id": 2, 
      "img_url": "a"
    }, 
    {
      "category": 1, 
      "description": "a", 
      "headline": "a", 
      "id": 3, 
      "img_url": "a"
    }, 
    {
      "category": 1, 
      "description": "a", 
      "headline": "a", 
      "id": 4, 
      "img_url": "a"
    }, 
    {
      "category": 1, 
      "description": "a", 
      "headline": "a", 
      "id": 5, 
      "img_url": "a"
    }
  ], 
  "success": true, 
  "total_news": 5
}
```

#### 2. GET /categories
Fetches all the categories

```json
{
  "categories": {
    "1": "Pakistan", 
    "2": "India", 
    "3": "Health"
  }, 
  "success": true
}
```

#### 3. GET /news/<news_id>
Fetches one news

```json
{
 "news": [
    {
      "category": 1, 
      "description": "a", 
      "headline": "a", 
      "id": 1, 
      "img_url": "a"
    }],
  "success": true
}
```

#### 4. POST /news/

Post a new

```json
{
  "success": "true",
  "created": 10,
  "news": [
    {
      "category": 1, 
      "description": "a", 
      "headline": "a", 
      "id": 1, 
      "img_url": "a"
    }, 
    {
      "category": 1, 
      "description": "a", 
      "headline": "a", 
      "id": 2, 
      "img_url": "a"
    }, 
    {
      "category": 1, 
      "description": "a", 
      "headline": "a", 
      "id": 3, 
      "img_url": "a"
    }, 
    {
      "category": 1, 
      "description": "a", 
      "headline": "a", 
      "id": 4, 
      "img_url": "a"
    }, 
    {
      "category": 1, 
      "description": "a", 
      "headline": "a", 
      "id": 5, 
      "img_url": "a"
    }
  ],
  "total_news": 5
}
```

#### 5. DELETE /news/<news_id>
Deletes a news
```json
{
  "total_news": 10,
 "deleted": 3,
  "success": true
}

```


#### 5. PATCH /news/<news_id>
Edits a news

```json

{
  "total_news": 10,
 "edited": 3,
  "success": true
}

```
