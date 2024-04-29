import paramiko
import os

SFTP_SERVER = os.getenv('SFTP_SERVER')
SFTP_USERNAME = os.getenv('SFTP_USERNAME')
SFTP_PASSWORD = os.getenv('SFTP_PASSWORD')


def get_sftp():
    transport = paramiko.Transport((SFTP_SERVER, 22))
    transport.connect(None, SFTP_USERNAME, SFTP_PASSWORD)
    sftp = paramiko.SFTPClient.from_transport(transport)

    return sftp
