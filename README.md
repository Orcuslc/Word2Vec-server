#Word2Vec-API

This Server-Client structure is forked from https://github.com/3Top/word2vec-api/blob/master/word2vec-api.py, and was added some functions to satisfy our needs.

* Launching Service
```
python nserver.py --model /PATH/TO/MODEL --concept /PATH/TO/CONCEPT [--host host] [--port integer]
```
* Example Calls
  * Direct Call
  ```
  curl http://127.0.0.1:5000/word2vec/msc?word=apple
  return: "fruit"
  ```
  ```
  curl http://127.0.0.1:5000/word2vec/sc?word=apple
  return: A list containing the sim('apple', attr) for attr in concept list
  ```
  * Indirect Call：
  Write the words in ```./words```, with each word in a line
  ```
  python3 test.py method('sc' or 'msc')
  return: the length of ./words ,total time cost
  ```
  The result will be in ```./result```
  
