# AutoNFT Marketeer
Make a word into commercial stories
---
## Get started

## Get virtual env
```shell
python3 -m venv env
source env/bin/activate
```
### Install packages
```shell
pip install -r requirements.txt
```

### Start the server
```shell
flask --app server run
```
---
## Structure
### 1. `/make-stores`
To receive the story request. 
#### The example of JSON request
```json
{
    "word": "French Pizza Restaurant",
    "n_sentences": 3
}
```
#### The example of JSON response
```json
[
    {
        "id": 1,
        "sentence": "French protesters carry french flags and walk to the french restaurant."
    },
    {
        "id": 2,
        "sentence": "A frenchman is eating a pizza in the restaurant in Paris."
    },
    {
        "id": 3,
        "sentence": "A boy is eating a big camembert pizza with his mother in pizza restaurant."
    }
]
```