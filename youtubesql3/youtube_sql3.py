import sqlite3 as db

conn = db.connect("youtube.db")
cursor = conn.cursor()

cursor.execute(
    '''
    CREATE TABLE IF NOT EXISTS videos (
               id INTEGER PRIMARY KEY,
               name TEXT NOT NULL,
               time TEXT NOT NULL
    )
'''
)
def list_videos():
    cursor.execute("SELECT * FROM videos")
    for row in cursor.fetchall():
     if row != []:
            print(row) 
    else :
            print("no data")
           


def add_videoes(name, time):
    cursor.execute("INSERT INTO videos (name, time) VALUES (?, ?)", (name, time))
    conn.commit()

def update_video(new_name,new_time,video_id):
    cursor.execute("UPDATE videos SET name = ?, time = ? WHERE id = ?", (new_name, new_time, video_id))
    conn.commit()

def delete_entry(video_id):
    cursor.execute("DELETE FROM videos WHERE id = ? " , (video_id))
    conn.commit()

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
# <<<<<<<<<<<<<<  ✨ Codeium Command 🌟 >>>>>>>>>>>>>>>>
                print("existing the app")
                


if __name__ == "__main__":
    main()                