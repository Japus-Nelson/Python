import pdb
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
            if count:
                print(f'password appeared in pwned search totally {count} times. Try changing new')
                return count
    return f'Congrats, Your password is complaint and doesnt appeared in any pwned searches{0}'


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
    leak_count = get_password_leak_count(response, tail)
    print(leak_count)


def main(args):
    for password in args:
        pass_hashing(password)


main(sys.argv[1:])
