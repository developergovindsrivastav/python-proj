import json
def load_data():
    try:
        with open("youtube.txt",'r') as file :
             text = json.load(file)
             return text 
    except FileNotFoundError:
             return print("file not found in your list")        
videos = load_data()             
def add_saver(content):
    with open("youtube.txt", 'w') as file:
        json.dump(content,file) 



def list_all_videos():
        print("\n")
        print("list of all videos : ")
        print("\n")
        print("*" * 70)
        for index,video in enumerate(videos,start=1):
         print(f"{index}. Name:{video['name']}, Duration: {video['duration']} ")  
        print("*" * 70)



def add_videos(hello):
    name = input("enter the name : ")
    duration = input("enter the duration : ")
    content = ({'name':name, 'duration' : duration})
    hello.append(content)
    add_saver(hello)
    print('\n')
    print("your video is added successfully")
    print('\n')

def update_entry():
  index = int(input("enter the index of the video you want to update : "))
  if  1  <= index <= len(videos) :
      name = input("enter the new name : ")
      duration = input("enter the new duration : ")
      videos[index - 1] = {'name': name, 'duration': duration}
      add_saver(videos)


def delete_entry():
    list_all_videos()
    index = int(input("enter the index of the video you want to delete : "))
    if  1  <= index <= len(videos) :
        del videos[index - 1]
        add_saver(videos)
    else:
        print("invalid index".capitalize())      
        




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
                list_all_videos()
            case '2':
                add_videos(videos)    
            case '3':
                update_entry()
            case '4':
                delete_entry()    
            case '5':

                print("\n")
                print("*" * 70)
                print("thank you for using the app")
                print("\n")
                break  
            case _:
                print("invalid input".capitalize())      

if __name__ == "__main__":
    main()          

