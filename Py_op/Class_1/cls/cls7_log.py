##1.

class ContactList(list):
    def search(self, name):
        """Return all contacts that contain the search value
        in their name."""
        matching_contacts = []
        for contact in self:
            if name in contact.name:
                matching_contacts.append(contact)
        return matching_contacts

class Contact:
    all_contacts = ContactList()

    def __init__(self, name, email):
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)

# class Contact:
#     all_contacts = []
#
#     def __init__(self, name, email):
#         self.name = name
#         self.email = email
#         Contact.all_contacts.append(self)


c1 = Contact("QA STA", "QAa@litepoint.com")
c2 = Contact("QA STB", "QAb@litepoint.com")
c3 = Contact("QA STC", "QAc@litepoint.com")
rst = [c.name for c in Contact.all_contacts.search('QA')]
#print(rst)
# ['QA STA', 'QA STB', 'QA STC']

class LongNameDict(dict):
    def longest_key(self):
        longest = None
        for key in self:
            if not longest or len(key) > len(longest):
                longest = key
        return longest

longkeys = LongNameDict()
longkeys['wifi'] = 1
longkeys['ac'] = 2
longkeys['11abgn'] = 3
longkeys['11ax-rsdb'] =4
rst1 = longkeys.longest_key()
print(rst1)
# 11ax-rsdb