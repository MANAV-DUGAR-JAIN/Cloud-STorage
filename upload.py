import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        """upload a file to Dropbox using API v2
        """
        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'sl.BCXj3ZcCWj8WR76I5lSZhAMEST-pM-nfLXoAomCOrcAQtc-kupDOBQXES3taV58aqWo9fsVPpIAMOrcDX7xfWa6xATw92k4lsTUptBAsmzQWNnd7GV15T19PjG7c4jm5rt0BkTg' 
    transferData = TransferData(access_token)

    file_from = 'text1.txt'
    file_to = '/Upload_Dataa/text1.txt'  # The full path to upload the file to, including the file name

    # API v2
    transferData.upload_file(file_from, file_to)
    print("File has been Moveddddddddd! :-D")

main()  