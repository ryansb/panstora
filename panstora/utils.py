import cryptacular.bcrypt
crypt = cryptacular.bcrypt.BCRYPTPasswordManager()

alphabet = ('0123456789abcdefghijkmnopqrstuvwxyz'
            'ABCDEFGHJKLMNPQRSTUVWXYZ')
base_count = len(alphabet)


def encode62(num):
    """ Returns num in a base62-encoded string """
    encode = ''

    if (num < 0):
        return ''

    while (num >= base_count):
        mod = num % base_count
        encode = alphabet[mod] + encode
        num = num / base_count

    if (num):
        encode = alphabet[num] + encode

    return encode


def decode62(s):
    """ Decodes the base62-encoded string s into an integer """
    decoded = 0
    multi = 1
    s = s[::-1]
    for char in s:
        decoded += multi * alphabet.index(char)
        multi = multi * base_count

    return decoded


def hash_password(password):
    return unicode(crypt.encode(password))
