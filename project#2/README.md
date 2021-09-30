# EC601 project2
Twitter API & Google NLP API

@https://github.com/twitterdev/Twitter-API-v2-sample-code
@https://console.cloud.google.com/natural-language/locations/us-central1/datasets/TCN4475228379083177984;modelId=TCN3596394782315773952/predict?project=ec601-327421

1. Look up tweets with detailed information by certain Ids, look up  twitter users, look up liking users
and get followers.

Before use these source files, some packages need to be installed as below.
Run commands in terminal:
pip install requests
pip install twarc

A test of users_lookup.py: I entered Boston University ECE and got its created time, id, location and so on.

![image](https://user-images.githubusercontent.com/80809231/134821163-a5daf795-709f-4222-8e2e-716c56a74519.png)

A test of tweetslookup.py: I entered the id of one of Joe Biden's tweets and got its detailed information.

![image](https://user-images.githubusercontent.com/80809231/134821795-2d51170e-2bd1-489c-8c04-7e35c2ee2654.png)

2. Build and deploy custom machine learning models that analyze documents, categorizing them, identify entities within them, or assessing attitudes within them.

With a single-label classification training in Google NLP API, I implemented a test for a text:
![image](https://user-images.githubusercontent.com/80809231/135372330-ce79182f-8d5d-4594-aaea-fcbb582b226f.png)
