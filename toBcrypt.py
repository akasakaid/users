import bcrypt

user = input('- input user : ')
code_app = input('- input code app : ')
name = input('- input name : ')
garam = bcrypt.gensalt()
auth = user + code_app + name
create = bcrypt.hashpw(bytes(auth,'utf-8'),garam).decode('utf-8')
print(create)
