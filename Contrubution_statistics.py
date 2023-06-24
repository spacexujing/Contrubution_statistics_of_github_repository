from github import Github
from github import Auth

auth = Auth.Token('your github token') # change it with your own github token. 换成你自己的github token 
g = Github(auth=auth)
project_path='spacexujing/Contrubution_statistics_of_github_repository' # change it with your own repository path. 换成你自己的仓库地址
repo = g.get_repo(project_path)

pull_requests = repo.get_pulls(state='all')
d={}
for pr in pull_requests:
    # Only collect the request that merged. 
    # If you want to collect every request, just comment out.
    # 只统计merged的request。想统计全部就注释掉这一段。
    merged=pr.merged
    if not merged:
        continue

    author = pr.user.login
    if author not in d:
        company=pr.user.company
        email=pr.user.email
        d[author]={'company':company,'email':email,'additions':0,'deletions':0,'pr_count':0}
    
    additions = pr.additions
    deletions = pr.deletions

    d[author]['additions']+=additions
    d[author]['deletions']+=deletions
    d[author]['pr_count']+=1

csvContent='author,company,email,additions,deletions,pr_count\n'
for author,info in d.items():
    csvContent+=author+','+str(info['company'])+','+str(info['email'])+','+str(info['additions'])+','+str(info['deletions'])+','+str(info['pr_count'])+'\n'

fileName=".\\output.csv"
with open(fileName,"w") as csv_file:
	csv_file.write(csvContent)
