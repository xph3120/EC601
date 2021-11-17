from twarc import Twarc2, expansions
import json

# Replace your bearer token below
client = Twarc2(bearer_token="AAAAAAAAAAAAAAAAAAAAAK1KUAEAAAAA0i6%2BDVzO%2FOH7V%2BlwRmFkZ6FFwQE%3D4MWi6AI6QUNziosBq3FKNXJKljpIQsjiqc86W940MuR9M5U5zw")


def main():
    # The followers function gets followers for specified user
    followers = client.followers(user="yaojilaosun")
    for page in followers:
        result = expansions.flatten(page)
        for user in result:
            # Here we are printing the full Tweet object JSON to the console
            print(json.dumps(user))


if __name__ == "__main__":
    main()