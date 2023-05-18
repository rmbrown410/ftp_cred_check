import ftplib
import argparse
import itertools

parser = argparse.ArgumentParser()

parser.add_argument("-ul", "--username_list",
                    dest="ul",
                    help="Use a username input list",
                    action='store')
parser.add_argument("-pl", "--password_list",
                    dest="pl",
                    help="Use a password input list",
                    action='store')
parser.add_argument("-url", "--target_ftp_server",
                    dest="url",
                    help="Link to ftp server",
                    action='store')

args = parser.parse_args()
ul = args.ul if args.ul else None
pl = args.pl if args.pl else None
url = args.url if args.url else None

def check(ul, pl, url):
    timeout = 3
    try:
        ftp = ftplib.FTP(url, ul, pl)
        ftp.login(ul,pl)
        print(ul+': Login was successful')
        ftp.quit()
        result = True
    except Exception as e:
        # print(ul+" EXCEPTION::::--> " + str(e))
        print(ul+": " + str(e))
        result = False
    # print(result)
    return(result)
    

def main(ul=ul, pl=pl, url=url):
    if ul:
        usernameList = []
        try:
            f_file = open(str(ul), 'r')
            usernameList = f_file.read().replace('\r', '').split('\n')
            try:
                usernameList.remove('')
            except ValueError:
                pass
                f_file.close()
        except:
            print('Error reading file')
            exit(1)
    if pl:
        passwordList = []
        try:
            f_file = open(str(pl), 'r')
            passwordList = f_file.read().replace('\r', '').split('\n')
            try:
                passwordList.remove('')
            except ValueError:
                pass
                f_file.close()
        except:
            print('Error reading file')
            exit(1)

        for (a, b) in zip(usernameList, passwordList):
            result = check(a, b, url)

    print('[%] Done.')

if __name__ == '__main__':
    try:
        main(ul=ul, pl=pl, url=url)
    except KeyboardInterrupt:
        print('\nKeyboardInterrupt Detected.')
        print('Exiting...')
        exit(0)