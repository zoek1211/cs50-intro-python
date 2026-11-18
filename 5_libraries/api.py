import requests

# https://api.artic.edu/docs/#collections 


def main():
    print("Search the Art Institute of Chicago")
    artist = input("Artist: ") # get artist name from user 

    try:
        # http get request
        response = requests.get(
            "https://api.artic.edu/api/v1/artworks/search", 
            {"q": artist} # type in search query 
            )
        # print((response)) # response 200 means ok
        response.raise_for_status() # raise error for bad response
    except request.HTTPError:
        print("could not complete request")
        return
    
    content = response.json() # convert to json format
    # print(content)

    # read the documentation to use keys properly 
    for artwork in content["data"]: # key "data" contains list of artworks
        print(f"* {artwork['title']}") # print title of each artwork


main()