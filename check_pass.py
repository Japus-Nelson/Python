# import pdb
import sys             #for getting input from user
import requests       #module to interact as a browser api
import hashlib        # to hash our password

# We give first 5 digits of our hashed password, It will search the db for the passwords that matches the 5 strings,
# and provides the matching output of the 5 strings.
#k-anonymity will let others know your information, but still they will not who you are, we can read the response from the data, web
# and filter out how many times our password was leaked.


def request_api_data(query_api):
    url = 'https://api.pwnedpasswords.com/range/' + query_api
    res = requests.get(url)
    # print(res.status_code)
    if res.status_code != 200:
        raise RuntimeError(f'Error Fetching {requests.status_codes}, Try entering different passwords')
    return res


def get_password_leak_count(hexapass, tail_pass):
    hashes = (lines.split(':') for lines in (hexapass.text.splitlines()))
    for h, count in hashes:
        if h == tail_pass:
            return count
    return 0


def pass_hashing(password):

    #encode the password, then hashed it using sha1 algorithm, and digest using hexadigest
    encrypted = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    # unpacking the password to travers it through the code
    first_5, tail = (encrypted[0:5], encrypted[5:])
    print(first_5, tail)
    # passing our unpacked first_5 password in to the api to check our password been pwned or not?
    response = request_api_data(first_5)
    print(response)
    # checking the passwords leaked count
    return get_password_leak_count(response, tail)



def main(args):
    for password in args:
        print(password)
        count = (pass_hashing(password))
        print(count)
        if count:
            print(f' Your password {password} has appeared {count} many times. Consider changing the password')
        else:
            print(f'congrats!. Your {password} was not pwned. It is secure')
    return 'done!'


#To be more secure! Read the passwords from the text file.
input_text = open(r"C:\Users\japus\Downloads\text.txt", 'r').read()
read = input_text.splitlines()


if __name__ == '__main__':
    sys.exit(main(read))
