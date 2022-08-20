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
### 1. `/what`
To receive the story request. 
#### The example of JSON request
```json
{
    "question": "a man named neo tried to find out if he hs in a simulation",
    "topic": "movie"
}
```
#### The example of JSON response
```json
{
    "answer": "The matrix"
}
```
#### Locally test with curl
```shell
curl -X POST "https://whatis-server-xlqc3o3mha-ew.a.run.app/what"\
   -H 'Content-Type: application/json'\
   -d '{"question":"a man who is born in a cave and kidnapped by a monkey","topic":"movie"}'
```
