from pymongo import MongoClient as mongo
from bson import ObjectId as id
try:
    client = mongo("mongodb://localhost:27017")
    db = client["youtube"]
    video_collection = db["videos"]
    # print(video_collection)
except Exception as e:
    print(e)
def list_videos():
   for video in  video_collection.find():
       print(f"name: {video['name']}, time: {video['time']}, id : {video['_id']}")
def add_videoes(name,time):
    video_collection.insert_one({"name":name,"time":time})
def update_video(new_name,new_time,video_id):
    video_collection.update_one({"_id":id(video_id)},{"$set":{"name":new_name,"time":new_time}})
def delete_entry(video_id):
    video_collection.delete_one({"_id":id(video_id)})


def main():
    while True:
        print("welcome to youtube helper ")
        print("1. list all the added videos")
        print("2. add the video")
        print("3. update the existing entry")
        print("4. delete the added video")
        print("5. exit the app")
        choice_of_user = input("select your choice : ")
        match choice_of_user:
            case '1':
                list_videos()
            case '2':
                name = input("enter the name: ")
                time = input("enter the time: ")
                add_videoes(name, time)
            case '3':
                new_name = input("enter the name: ")
                new_time = input("enter the time: ")
                video_id = input("enter the id: ")
                update_video(new_name,new_time,video_id)
            case '4':
                video_id = input("enter the id: ")
                delete_entry(video_id)
            case '5':
                print("\n")
                print("existing the app")    

if __name__ == "__main__":
    main()
