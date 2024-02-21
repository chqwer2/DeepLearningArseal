



# 我们需要获取Google Service API的身份验证文件

# pip install pydrive



from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

# Rename the downloaded JSON file to client_secrets.json
# The client_secrets.json file needs to be in the same directory as the script.
gauth = GoogleAuth()
auth_url = gauth.GetAuthUrl() # Create authentication url user needs to visit
code = AskUserToVisitLinkAndGiveCode(auth_url) # Your customized authentication flow
gauth.Auth(code) #


# List files in Google Drive
fileList = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()
for file1 in fileList:
  print('title: %s, id: %s' % (file1['title'], file1['id']))




# Ref to https://zhuanlan.zhihu.com/p/144808681


# Google Drive API:
# In this file -
#
# client_secret_44495293579-7d5obmkgrdcg9bvac7gj83ngnvu08uu0.apps.googleusercontent.com
# 我们需要把上面步骤中下载的JSON文件另存为client_serets.json文件，
# 并把它放到Python程序所在的存储文件下。



# 为了避免每次都填写用户名和密码，我们可以创建一个settings.yaml文件，如下所示完成相关设置。



