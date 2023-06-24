# Contrubution_statistics_of_github_repository
Collect statistics of the contrubution in a github repository.  
So you can easily figure out how many codes everyone contrubutes to that repository.  
It may take a long time. As it seems requests to github for every single info every time.  
There are a lot more elements in pr. You can get them in same way.  
You need "pip install pygithub",not "pip install github".  

统计github仓库里代码的贡献。能快速知道所有贡献者分别给仓库贡献了多少代码。  
虽说快速也是对人工的。实际可能会有点小慢，似乎拿每一个参数都得向github请求一次。也可能只是因为众所周知的原因导致我对github的请求速度比较慢。  
可以自己查看pr的内容来获得更多数据。  
代码本身不难。不过反正我都应需求写出来了，就上传了。
注意这个包用pip安装时应该是pip install pygithub。

Output would be like:  
![image](https://github.com/spacexujing/Contrubution_statistics_of_github_repository/assets/63943887/59dcb1bd-5b3f-4492-a5f3-8c93836e713b)  
None represents that info does not set in the account.   
None意味着TA的github账户上没有填这条信息。  
