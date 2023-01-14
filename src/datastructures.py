
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint


class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        # example list of members
        self._members = [
            {
                "id": self._generateId(),
                "first_name": "Jane",
                "last_name": last_name,
                "age": 35,
                "lucky_numbers": [10, 14, 3]
            },
            {
                "id": self._generateId(),
                "first_name": "John",
                "last_name": last_name,
                "age": 33,
                "lucky_numbers": [10, 14, 3]
            },
           {
                "id": self._generateId(),
                "first_name": "Jimmy",
                "last_name": last_name,
                "age": 5,
                "lucky_numbers": [1]
           }
        ]

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        member_to_add = {
            "id": member["id"] if member["id"] != None else self._generateId(),
            "first_name": member["first_name"],
            "last_name": self.last_name,
            "age": member["age"],
            "lucky_numbers": member["lucky_numbers"]
            }
        return self._members.append(member_to_add)

    def delete_member(self, id):
        # fill this method and update the return
        user_to_delete = list(filter(lambda miembro: miembro["id"]==id, self._members))
        userdelete = self._members.remove(user_to_delete)
        return self._members
    
    def update_member(self, id, member):
        id_to_update = list(filter(lambda m: m["id"]==id, self._members))
        member_to_update = self._members[id_to_update]
        member_to_update = member
        ##filtrar por id y añadir el member para update y append a self._members
        ## you have to implement this method
        ## loop the list and replace the member with the given id
        return self._members

    def get_member(self, id):
        # fill this method and update the return
        member_list = list(filter(lambda m: m["id"]==id, self._members))
        member = member_list[0]
        return member

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members
