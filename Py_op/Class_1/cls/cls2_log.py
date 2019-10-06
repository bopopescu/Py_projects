class ContactList(list):
    def search(self, name):
        '''Return all contacts that contain the search value
        in their name.'''
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
        self.all_contacts.append(self)

#________________________________________________________
class Supplier(Contact):
    def order(self, order):
        print("Send ""{} order to {}".format(order, self.name))

class Friend(Contact):

    def __init__(self,name, email, phone):
        super().__init__(name,email)
        self.phone = phone
        self.all_contacts.append(self)

        """
        self.name = name
        self.email = email
        self.phone = phone
        """

class LongNameDict(dict):
    def longest_key(self):
        longest = None
        for key in self:
            if not longest or len(key)  > len(longest):
                longest = key
        return longest

def main():
    c = Contact("tester, M16", "m16@litepoint.com")
    s = Supplier("tester,MW16", "MW@litepoint.com")
    ss = Supplier("fuji, 2800","2800@litepoint.com")
    # f = Friend("Foxcon, 2200", "M8@litepoint.com","408-334-8800")

    name_list = [item.name for item in Contact.all_contacts.search('tester')]
    print(name_list)
    s.order("SMA cables")
    print(s.all_contacts)
    print(s)
    print()
    longestkeys = LongNameDict()
    longestkeys["wifi"] = 1
    longestkeys["ax"] = 2
    longestkeys['ac &  n & abg']  =3
    print(longestkeys.longest_key())


if __name__ == '__main__':
    main()


# ['tester, M16', 'tester,MW16']
# Send SMA cables order to tester, MW16
# [ < __main__.Contact object at 0x007C0BF0 > , < __main__.Supplier object at 0x007C0C50 > , < __main__.Supplier object at 0x007C0C70 > , < __main__.Friend object at 0x007C0C90 > , < __main__.Friend object at 0x007C0C90 > ]
# <__main__.Supplier object at 0x007C0C50 >

# ac & n & abg


#     ['tester,M16', 'tester,MW16']
# Send SMA cables order to tester, MW16
# [ < __main__.Contact object at 0x03470BF0 > , < __main__.Supplier object at 0x03470C50 > , < __main__.Supplier object at 0x03470C70 > , < __main__.Friend object at 0x03470C90 > , < __main__.Friend object at 0x03470C90 > ]
# <__main__.Supplier object at 0x03470C50 >

# ac & n & abg
