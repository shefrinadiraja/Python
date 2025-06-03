import sqlite3



def get_image_from_userid(user_id):
    db_connection = sqlite3.connect('/Users/thahazykandy/Desktop/Python/social_data_project/photo_app.db')
    db_cur = db_connection.cursor()
    db_cur.execute('select * from images where user_id =?', (user_id,)   )
    data = db_cur.fetchall()
    print(data)
    return data

abc = input('Enter User number: ')
get_image_from_userid(abc)


# based on image id we will get comments on image

def get_comment_by_imge_id(image_id):
    db_connection = sqlite3.connect('/Users/thahazykandy/Desktop/Python/social_data_project/photo_app.db')
    db_cur = db_connection.cursor()
    db_cur.execute('select * from comments where image_id =?', (image_id,)   )
    data = db_cur.fetchall()
    print(data)
    return data




abc = input('Enter image number: ')
get_comment_by_imge_id(abc)

# based on image id we will get comments on image

def who_is_user(id):
    db_connection = sqlite3.connect('/Users/thahazykandy/Desktop/Python/social_data_project/photo_app.db')
    db_cur = db_connection.cursor()
    db_cur.execute('select * from users where id =?', (id,)   )
    data = db_cur.fetchall()
    print(data)
    return data


abc = input('Enter user_number_who_commend: ')
who_is_user(abc)