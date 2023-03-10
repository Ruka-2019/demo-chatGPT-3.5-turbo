## Description
An example of using openai `gpt-3.5-turbo` model and api to build chatGPT like chatbot from code.
Here is an example of the usage using this script. It is able to trace the chat history as the web version did.

For more info on this api check out [OpenAI GPT-3.5 Turbo API](https://platform.openai.com/docs/guides/chat).


```terminal
User: show me the code to solve the famous algraisom problem 'fizz buzz'
ChatGPT: Here's the code to solve the "FizzBuzz" problem:

python
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

This code prints the numbers from 1 to 100, but for multiples of 3 it prints "Fizz" instead of the number, and for multiples of 5 it prints "Buzz". For numbers which are multiples of both 3 and 5, it prints "FizzBuzz".
User: now change the problem from multiples of 3 to  multiples of 4, then update the code you provide
ChatGPT: Sure, here is the code that solves the problem of multiples of 4 instead of multiples of 3:

python
for i in range(1, 101):
    if i % 4 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 4 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)


This code is similar to the previous one, but it checks for multiples of 4 instead of multiples of 3. For multiples of 4, it prints "Fizz", for multiples of 5, it prints "Buzz", and for those multiples of both, it prints "FizzBuzz".


```

## Install

run following command to install openai library
```
pip install openai
```

then replace the `openai.api_key = "YOUR_OPENAI_API_KEY"` to your api key.

