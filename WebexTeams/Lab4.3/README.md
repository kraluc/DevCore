# Testing 3rd party APIs

The lab relies on the Mock library

Tutorial: [Mocking External APIs in Python](https://realpython.com/testing-third-party-apis-with-mocks/)

```
pip install nose requests
```

For this tutorial, you will be communicating with a fake online API that was built for testing - [JSON Placeholder](http://jsonplaceholder.typicode.com/)

```bash
❯ curl -X GET 'http://jsonplaceholder.typicode.com/todos'
< snip >
[
  {
    "userId": 1,
    "id": 1,
    "title": "delectus aut autem",
    "completed": false
  },
  < snip>
    {
    "userId": 10,
    "id": 200,
    "title": "ipsam aperiam voluptates qui",
    "completed": false
  }
]
  ```
