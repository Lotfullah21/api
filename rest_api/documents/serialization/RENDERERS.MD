## Renderers

there are different data types that can be returned from an `API`.
renderers are responsible for displaying the output of our `APIs`.

### Built-in renderers

- `JSONRenderer`: displays JSON data
- `BrowsableAPIRenderer`: displays browsable data

### Third Party renderers

- `XML Renderer`:
- `YAML Renderer`
- `JSONP Renderer`

by default `DRF` uses two renderers `JSONRenderer` and `BrowsableAPIRenderer`.

to initialize the type of renderers, add the following code in settings.py, DRF uses this code to initialize the type of APIs output data.

```py
REST_FRAMEWORK= {
    'DEFAULT_RENDERER_CLASSES':[
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer'
    ]
}
```

as a client, we need to add in the header in which format, we want our data to be in.

some common header types

```table
| Accept Header                | Description                                       |
|------------------------------|---------------------------------------------------|
| `Accept: application/json`    | Expect JSON response.                             |
| `Accept: application/xml`     | Expect XML response.                              |
| `Accept: text/xml`            | Expect XML response (alternative format).        |
| `Accept: text/html`           | Expect HTML response (Browsable API).             |
| `Accept: text/plain`          | Expect plain text response.                       |
| `Accept: application/octet-stream` | Expect binary data response.              |

```

to add another support, let's say `XML`, first we need to install it,

```sh
pip install djangorestframework-xml
```

```py
#settings.py
REST_FRAMEWORK= {
    'DEFAULT_RENDERER_CLASSES':[
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer'
    ]
}
```
