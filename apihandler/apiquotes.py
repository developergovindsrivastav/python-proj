import requests
def fetch_data_in_api():
    url = "https://api.freeapi.app/api/v1/public/quotes?page=1&limit=10&query=human"
    data = requests.get(url)
    data_json = data.json()
    content_in_data = data_json["data"]
    data_in_data = content_in_data["data"]
    status_code = data_json["success"]
    if status_code == True and data_in_data != None:
           data_array = data_in_data[1]
           data_author = data_array["author"]
           data_content = data_array["content"]
           return [data_author,data_content]
    else:
                raise Exception("failed to fetch data")

def main():
      try:
         author = fetch_data_in_api()[0]
         content = fetch_data_in_api()[1]
         print(f"author : {author} \n content: {content}")
      except Exception as e :
        print(str(e))


if __name__ == "__main__":
    main()