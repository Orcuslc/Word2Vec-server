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
  python3 test.py method(sc or msc) /PATH/TO/WORDS /PATH/TO/RESULT(default: ./results)
  return: the length of ./words ,total time cost
  ```
  <!-- The result will be in ```./result``` -->
  
* Results
  * When method is ```msc```:
    For direct call, the result will be a string of the most similar word in the concepts.
    For indirect call, the result will be in ```./results(default)``` or the input path. Each line contains the result of a word.
  * When method is ```sc```:
    For direct call, the result will be a list of similarity of the input word with each word in the concepts.
    For indirect call, each line of the results file contains the result of a word.
  * If the result of direct/indirect call is 0, that means the input word is not in the model's vocabulary.