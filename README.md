# Contrubution_statistics_of_github_repository
Collect statistics of the contrubution in a github repository.  
So you can easily figure out how many codes everyone contrubutes to that repository.  
It may take a long time. As it seems requests to github for every single info every time.  
There are a lot more elements in pr. You can get them in same way.  

统计github仓库里代码的贡献。能快速知道所有贡献者分别给仓库贡献了多少代码。  
虽说快速也是对人工的。实际可能会有点小慢，似乎拿每一个参数都得向github请求一次。也可能只是因为众所周知的原因导致我对github的请求速度比较慢。  
可以自己查看pr的内容来获得更多数据。  
代码本身不难。不过反正我都应需求写出来了，就上传了。  

Output would be like:  
author	company	    email	        additions	deletions	pr_count  
A	    None	    AofA@gmail.com	2965	    1031	    21  
B	    company A	anyway@mail.com	1561	    1486	    19  
C	    company B	None	        5632	    1670	    18  
D	    None	    None	        8941	    537	        6  
E	    None	    None	        1498	    110	        5  
 
None represents that info does not set in the account.   
None意味着TA的github账户上没有填这条信息。  