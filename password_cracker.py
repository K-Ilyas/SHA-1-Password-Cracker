import hashlib


def crack_sha1_hash(hash, use_salts=False):

    passwords_file, matched_password, salts_file, salts = (
        open("./top-10000-passwords.txt"), "", "", [])

    passwords = [line.strip() for line in passwords_file.readlines()]

    passwords_file.close()

    if use_salts:
        salts_file = open("./known-salts.txt")
        salts = [line.strip() for line in salts_file.readlines()]
        salts_file.close()
        passwords = [(password, '{}{}'.format(password, salt), '{}{}'.format(salt, password))
                     for password in passwords for salt in salts]
        matched_password = next(filter((lambda x: (hashlib.sha1(x[1].encode()).hexdigest(
        ) == hash) or (hashlib.sha1(x[2].encode()).hexdigest(
        ) == hash)), passwords), "")
        matched_password = matched_password[0] if matched_password != "" else ""
    else:
        matched_password = next(filter(lambda x: hashlib.sha1(x.encode()).hexdigest(
        ) == hash, passwords), "")

    return matched_password if matched_password != "" else "PASSWORD NOT IN DATABASE"


# print(crack_sha1_hash("ea3f62d498e3b98557f9f9cd0d905028b3b019e1", True))
