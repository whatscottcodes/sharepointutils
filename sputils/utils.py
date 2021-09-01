from office365.runtime.auth.user_credential import UserCredential
from office365.runtime.auth.authentication_context import AuthenticationContext
from office365.sharepoint.client_context import ClientContext

import os

class spUtils:
    """
    Class for working with SharePoint files.
    """
    def __init__(self, username, password, baseurl):
        """
        Initialized with user's SharePoint username, password, and the SharePoint's baseurl.

        The user is then logged into a SharePoint session to use for uploading and downloading files.        
        """
        self.username = username
        self.password = password
        self.baseurl = baseurl
        self.ctx_auth = self.auth_user()

    def auth_user(self):
        ctx_auth = AuthenticationContext(self.baseurl)
        ctx_auth.acquire_token_for_user(self.username, self.password)

        return ctx_auth
    
    def get_file(self, siteName, spFolderPath, fileName, savePath):
    
        filePath = f"{savePath}/{fileName}"
        fullSiteName = "/sites/" + siteName
        siteurl = self.baseurl + fullSiteName 
        ctx = ClientContext(siteurl, self.ctx_auth)
        print("YO")
        localpath = filePath
        remotepath = f"{spFolderPath}/{fileName}"
    
        with open(filePath, "wb") as local_file:
            print("HI")
            print(f"{siteName}/{remotepath}")
            file = ctx.web.get_file_by_server_relative_url(f"{fullSiteName}/{remotepath}").download(local_file).execute_query()

        print("...file downloaded...")
        return filePath

    def upload_file(self, siteName, spFolderPath, fileName, filePath):
        filePath = f"{filePath}/{fileName}"
        fullSiteName = "/sites/" + siteName
        siteurl = self.baseurl + fullSiteName 
        ctx = ClientContext(siteurl, self.ctx_auth)
        
        localpath = filePath
        remotepath = f"{spFolderPath}{fileName}" # existing folder path under sharepoint site.
    
        with open(filePath, 'rb') as content_file:
            file_content = content_file.read()
        
        directory, name = os.path.split(remotepath)
    
        ctx.web.get_folder_by_server_relative_url(directory).upload_file(name, file_content).execute_query()
    
        try:
            ctx.web.get_file_by_server_relative_url(f"{fullSiteName}/{remotepath}").checkin(comment=" ", checkin_type=0)
            ctx.execute_query()
        except:
            print("...no check-in required...")
    
        print("...file uploaded...")