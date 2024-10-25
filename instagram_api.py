import time
import requests, json

class Trenstagram:
    def __init__(self, user_agent, cookies, email, username):
        self.BASE_URL = 'https://www.instagram.com/'
        self.USER_AGENT = user_agent
        self.session = requests.Session()
        self.session.headers = {'user-agent': self.USER_AGENT}
        self.session.headers.update({'Referer': self.BASE_URL + 'accounts/edit/'})
        self.session.headers.update({'X-CSRFToken': cookies['csrftoken']})
        
        self.email = email
        self.username = username

    def change_username(self, new_username):
        try:
            data = {
                'username': new_username,
                'email': self.email
            }
            r = self.session.post(self.BASE_URL + "accounts/edit/", data=data)
            if r.json()['status'] == "ok":
                print(f'Username Changed to {new_username}')
                self.username = new_username
                return True
            else:
                raise Exception()
        except:
            print('Error Changing Username')

    def change_bio(self, new_bio):
        try:
            data = {
                'username': self.username,
                'biography': new_bio,
                'email': self.email
            }
            r = self.session.post(self.BASE_URL + "accounts/edit/", data=data)
            if r.json()['status'] == "ok":
                print(f'Bio Changed to {new_bio}')
                return True
            else:
                raise Exception()
        except:
            print('Error Changing Bio')

    def change_name(self, new_name):
        try:
            data = {
                'username': self.username,
                'first_name': new_name,
                'email': self.email
            }
            r = self.session.post(self.BASE_URL + "accounts/edit/", data=data)
            if r.json()['status'] == "ok":
                print(f'Name Changed to {new_name}')
                return True
            else:
                raise Exception()
        except:
            print('Error Changing Name')
        
    def change_website(self, new_website):
        try:
            data = {
                'username': self.username,
                'external_url': new_website,
                'email': self.email
            }
            r = self.session.post(self.BASE_URL + "accounts/edit/", data=data)
            if r.json()['status'] == "ok":
                print(f'Website Changed to {new_website}')
                return True
            else:
                raise Exception()
        except:
            print('Error Changing Website')
        
    def change_profile_image(self, image_path):
        try:
            data = {
                "Content-Disposition": "form-data",
                "name": "profile_pic",
                "filename": "profilepic.jpg",
                "Content-Type": "image/jpeg"
            }
            with open(image_path, 'rb') as image_file:
                pfp = image_file.read()
                self.session.headers.update({'Content-Length': str(len(pfp))})
                r = self.session.post(self.BASE_URL + "accounts/web_change_profile_picture/", files={'profile_pic': pfp}, data=data)
                if r.json().get('changed_profile'):
                    print("Profile picture changed!")
                    return True
                else:
                    raise Exception()
        except Exception as e:
            print(f'Error Changing Profile Image: {e}')
            return False