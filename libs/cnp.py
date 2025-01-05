import bcrypt

def createNewPass(password):
    passBytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(passBytes, salt)
    decoded = hashed.decode('utf-8')
    print(decoded)
    return decoded;