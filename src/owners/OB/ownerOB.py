class ownerOB:

    def ownerOB(
        self,
        id_owner,
        name,
        last_name,
        age,
        id_number,
        owner_email,
        password,
        id_building,
    ):
        self.id_owner = id_owner
        self.name = name
        self.last_name = last_name
        self.age = age
        self.id_number = id_number
        self.owner_email = owner_email
        self.password = password
        self.id_building = id_building

    def get_id_owner(self):
        return self.id_owner

    def set_id_owner(self, id_owner):
        self.id_owner = id_owner

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_last_name(self):
        return self.last_name

    def set_last_name(self, last_name):
        self.last_name = last_name

    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age

    def get_id_number(self):
        return self.id_number

    def set_id_number(self, id_number):
        self.id_number = id_number

    def get_owner_email(self):
        return self.owner_email

    def set_owner_email(self, owner_email):
        self.owner_email = owner_email

    def get_password(self):
        return self.password

    def set_password(self, password):
        self.password = password

    def get_id_building(self):
        return self.id_building

    def set_id_building(self, id_building):
        self.id_building = id_building
