class User:
    def __init__(self, user_id, name):
        self._user_id = user_id
        self._name = name
        self._role = "user"

    def get_id(self):
        return self._user_id

    def get_name(self):
        return self._name

    def get_user_role(self):
        return self._role

    def set_name(self, name):
        self._name = name
        print("Имя изменено.")


class Admin(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name)
        self._role = "admin"

    def add_user(self, user_list, user):
        user_list.append(user)
        print(f"Пользователь {user.get_name()} добавлен.")

    def delete_user(self, user_list, user):
        user_list.remove(user)
        print(f"Пользователь {user.get_name()} удален.")

    def show_list(self, list):
        for user in list:
            print(f"Id:{user.get_id()} Name: {user.get_name()}")


users = []
admin = Admin(1, "Name0")
user1 = User(2, "Name1")
user2 = User(3, "Name2")
user3 = User(4, "Name3")

admin.add_user(users, user1)
admin.add_user(users, user2)
admin.add_user(users, user3)

admin.show_list(users)

user1.set_name("Name4")
admin.delete_user(users, user2)

admin.show_list(users)
