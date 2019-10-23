import datetime
import hashlib

the_hasher = None

def hash_this_with_date(data_to_hash, useDate=False):
    encoded_data = data_to_hash.encode('utf-8')
    the_hasher.update(encoded_data)
    if useDate:
        timestamp = datetime.datetime.now()
        the_hasher.update(str(timestamp).encode('utf-8'))
    return the_hasher.hexdigest()


# Function that asks the user for data to hash and prints out both the hash with date and without
def initiate_hashing():
    user_data = input("Enter data to generate the Hash Value:")
    returned_hash_with_date = hash_this_with_date(user_data, True)
    returned_hash_no_date = hash_this_with_date(user_data, False)
    print("Hash for data with Date: " + user_data + " is: " + returned_hash_with_date)
    print("Hash for data without Date: " + user_data + " is: " + returned_hash_no_date)


# perform basic checks, is a number
num_hashes = input("Enter the number of hashes to check: ")
try:
    num_hashes = int(num_hashes)
except ValueError:
    print("Invalid number specified, quitting")
    # quit the program if we have invalid data
    exit()

hash_mode = input("Select your choice of Hashing:\n 1. Sha1 \n 2: Sha224 \n 3: Sha256 \n 4: Sha384 \n 5: Blake2b \n 6: Blake2bs")
try:
    hash_mode = int(hash_mode)
except ValueError:
    print("Invalid Hash Mode entered, quitting.")
    exit()

if hash_mode == 1:
    the_hasher = hashlib.sha1()
elif hash_mode == 2:
    the_hasher = hashlib.sha3_224()
elif hash_mode == 3:
    the_hasher = hashlib.sha256()
elif hash_mode == 4:
    the_hasher = hashlib.sha384()
elif hash_mode == 5:
    the_hasher = hashlib.blake2b()
elif hash_mode == 6:
    the_hasher = hashlib.blake2s()
else:
    print("Invalid hashing option selected, quitting.")
    exit(-1)



counter = 0
while counter < num_hashes:
    initiate_hashing()
    counter +=1
