"""Module providingFunction: os tools."""
import os
from urllib.parse import urlparse
from shareplum import Site, Office365
from shareplum.site import Version
from loguru import logger
from injector import inject, singleton
from framework.set_up_environment import Config
from exceptions.exception import SystemException, BusinessException

@singleton
class SharePoint:
    """
    A class that represents a connection to a SharePoint site.

    This class provides methods for connecting to a SharePoint site and
    performing various operations, such as reading and writing data to lists
    and libraries, creating and updating site pages.
    """
    @inject
    def __init__(self, context: Config):
        self.context = context
        self.username = context.dict["ENV_SP_MAIL"]
        self.password = context.dict["ENV_SP_PASSWORD"]
        self.sharepoint_site = context.dict["ENV_SHAREPOINT_SITE"]
        self.sharepoint_doc = context.dict["ENV_SHAREPOINT_DOC_LIBRARY"]
        self.authcookie = None
        self.auth_site = None
        self.site = None
        self.sharepoint_dir = None
        self.folder = None
        self._folder = None
        
        parsed_url = urlparse(context.dict["ENV_SHAREPOINT_SITE"])
        base_url = parsed_url.scheme + '://' + parsed_url.netloc
        
        self.sharepoint_url = base_url
         
    def auth(self):
        """
        Authenticates with SharePoint using the provided username and password, and sets
        the authentication cookie and site object for subsequent API calls.

        Usage:
            my_sp_auth = SharePointAuth('https://my.sharepoint.com/', 'my_username', 'my_password')
            my_sp_auth.auth()

        Raises:
            ValueError: if authentication fails due to invalid credentials or network issues.
            Exception: if there is an unexpected error during authentication.
        """
        try:
            self.authcookie = Office365(self.sharepoint_url, username=self.username, password=self.password).GetCookies()
            self.site = Site(self.sharepoint_site, version=Version.v365, authcookie=self.authcookie, timeout=60)
        except ValueError as v_error:
            raise v_error
        except Exception as ex:
            raise SystemException("Unexpected error during authentication") from ex

        return self.site


    def connect_folder(self, folder_name):
        """
        Connects to the specified folder using the authentication obtained from the auth() function.

        Args:
            folder_name (str): The name of the folder to connect to.

        Returns:
            bool: True if the connection was successful, False otherwise.
        """
        self.auth_site = self.auth()

        self.sharepoint_dir = '/'.join([self.sharepoint_doc, folder_name])
        self.folder = self.auth_site.Folder(self.sharepoint_dir) # type: ignore
        logger.info(f"Connection to folder {folder_name} was sucess")
        return self.folder


    def upload_file(self, file, file_name, folder_name):
        """
        Uploads the specified file to the given folder.

        Args:
            file (bytes): The contents of the file.
            file_name (str): The name of the file to be uploaded.
            folder_name (str): The name of the folder to which the file will be uploaded.

        Raises:
            SystemException: If the file cannot be uploaded.
        """
        logger.info(f"Uploading file {file_name}, to: {folder_name}")

        try:
            self._folder = self.connect_folder(folder_name)
        except Exception as ex:
            raise BusinessException(ex) from ex

        try:
            with open(file, mode='rb') as file_obj:
                file_content = file_obj.read()

            self._folder.upload_file(file_content, file_name)

            sharepoint_url = os.path.join(self.sharepoint_site, self.sharepoint_doc, folder_name)
            logger.info(f"File was uploaded to URL: {sharepoint_url}")
            return sharepoint_url
        except Exception as ex:
            raise SystemException("Error occurred while uploading the file") from ex


    def delete_file(self, file_name, folder_name):
        """
        Deletes the specified file from the given folder.

        Args:
            file_name (str): The name of the file to be deleted.
            folder_name (str): The name of the folder containing the file.

        Raises:
            SystemException: If the file cannot be deleted.
        """
        logger.info(f"Removing file {file_name}, from the folder: {folder_name}")
        try:
            self._folder = self.connect_folder(folder_name)
            self._folder.delete_file(file_name)
            logger.info("File was removed")
        except Exception as ex:
            raise SystemException("Error occurred while deleting the file") from ex


    def get_file(self, file_name, folder_name):
        """
        Retrieves a file from the specified folder.

        Args:
            file_name (str): The name of the file to retrieve.
            folder_name (str): The name of the folder containing the file.

        Returns:
            bytes: The contents of the file as a byte string.

        Raises:
            SystemException: If an error occurs while retrieving the file.
        """
        logger.info(f"Get file {file_name}, from the folder: {folder_name}")
        try:
            self._folder = self.connect_folder(folder_name)
            file = self._folder.get_file(file_name)
            output_file_path = os.path.join(self.context.dict["temp_folder"], file_name)
            with open(output_file_path, "wb") as output_file:
                output_file.write(file)
            return output_file_path
        except Exception as ex:
            raise SystemException("Error occurred while getting the file") from ex