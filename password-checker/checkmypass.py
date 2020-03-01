# requests allows you to make web requests
import requests
import hashlib
import sys

# pwned api wants first 5 char of sha1 of password
def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f'Error fetching: {res.status_code}, check API and try again')
    return res

# response holds a list of all hashes and number of times pwned
def get_password_leaks_count(hashes, hash_to_check):
    # split the full hash from the number of  times pwned
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashes:
        # if the hash matches ours
        if  h == hash_to_check:
            return count
    return 0


def pwned_api_check(password):
    # get the sha1 of password
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    # grab first 5 and rest of string
    first5_char, tail = sha1password[:5], sha1password[5:]
    response = request_api_data(first5_char)
    return get_password_leaks_count(response, tail)

def main(args):
    for password in args:
        count = pwned_api_check(password)
        if count:
            print(f'{password} was found {count} times...you should change it')
        else:
            print(f'{password} was not found, carry on!')
        return 'done!'

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
