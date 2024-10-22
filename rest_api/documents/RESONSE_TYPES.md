## Response types:

We should allow developers to get the data based on their preference, this can be done by attaching `accept: value` variables in headers request from client side.

- `Accept: application/json`
- `Accept: application/xml`
- `Accept: text/xml`

based on accept value, the response should be delivered in that format only.

### Javascript object notation (JSON)

JSON data types are simple and lightweight and can be treated as object when reading or writing it and also creating and parsing of a json data is easier.
XML is more readable and supports attributes that are not possible with JSON.

#### Json vs xml

```table
| Feature              | JSON                                            | XML                                                          |
| -------------------- | ----------------------------------------------- | ------------------------------------------------------------ |
| Format               | Lightweight, key-value based                    | Tag-based, similar to HTML                                   |
| Syntax               | Key-value pairs                                 | Tags and attributes                                          |
| Example              | `{"author": "Jack London", "title": "Seawolf"}` | `<author>Jack London</author><title>Seawolf</title>`         |
| Bandwidth Usage      | Smaller, takes less bandwidth                   | Larger, takes more bandwidth                                 |
| Data Complexity      | Simple, with key-value structures               | Can be fairly complex                                        |
| Array Representation | Simple and concise                              | Verbose                                                      |
| Array Example        | `{"items": [1,2,3,4,5]}`                        | `<items><element>1</element>...<element>5</element></items>` |
| Parsing Speed        | Faster, requires less memory                    | Slower, requires more processing power                       |
| Comments             | No support for comments                         | Supports comments                                            |

```

<figure>
<img src="./images/client-server.png" height="390" width="862" alt="start">
<figcaption><p align="center">client-sever request-response cycle</p><figcaption>
</figure>
