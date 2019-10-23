import datetime
import hashlib


def hash_this_with_date(data_to_hash, useDate=False):
    encoded_data = data_to_hash.encode('utf-8')
    the_hasher = hashlib.sha256()
    the_hasher.update(encoded_data)
    if useDate:
        timestamp = datetime.datetime.now()
        the_hasher.update(str(timestamp).encode('utf-8'))
    return the_hasher.hexdigest()


user_data = input("Enter data to generate the Hash Value:")
returned_hash_with_date = hash_this_with_date(user_data, True)
returned_hash_no_date = hash_this_with_date(user_data, False)
print("Hash for data with Date included: " + user_data + " is: " + returned_hash_with_date)
print("Hash for data without date included: " + user_data + " is: " + returned_hash_no_date)