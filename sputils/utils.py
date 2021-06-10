from office365.runtime.auth.user_credential import UserCredential
from office365.runtime.auth.authentication_context import AuthenticationContext
from office365.sharepoint.client_context import ClientContext

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
        self.ctx_auth = auth_user(self)
        self.ctx = ClientContext(siteurl, ctx_auth)

    def auth_user(self):
        ctx_auth = AuthenticationContext(self.baseurl)
        ctx_auth.acquire_token_for_user(self.username, self.password)

        return ctx_auth
    
    def get_file(self, basesite, spfolderpath, fileName, savePath):
    
        filePath = f"{savePath}/{fileName}"
        siteurl = self.baseurl + basesite 
    
        localpath = filePath
        remotepath = f"{spFolderPath}/{fileName}"
    
        with open(filePath, "wb") as local_file:
            file = self.ctx.web.get_file_by_server_relative_url(f"{basesite}/{remotepath}").download(local_file).execute_query()
    
        return filePath

    def upload_file(self, basesite, spfolderpath, fileName, filePath, first_of_week):
        filePath = f"{filePath}/{fileName}"
        siteurl = self.baseurl + basesite 

        localpath = filePath
        remotepath = f"{spfolderpath}{fileName}" # existing folder path under sharepoint site.
    
        with open(filePath, 'rb') as content_file:
            file_content = content_file.read()
        
        directory, name = os.path.split(remotepath)
    
        self.ctx.web.get_folder_by_server_relative_url(directory).upload_file(name, file_content).execute_query()
    
        try:
            self.ctx.web.get_file_by_server_relative_url(f"{basesite}/{remotepath}").checkin(comment=" ", checkin_type=0)
            self.ctx.execute_query()
        except:
            print("...no check-in required...")
    
        print("...file uploaded...")