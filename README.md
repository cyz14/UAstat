# UAstat
Use python lib to do UserAgent parse and get statistics

# Task 1
统计IP的特征，比如单个IP对应的操作系统分布，浏览器分布，服务分布，传输数据的大小分布。
在requests文件中包含 os，browser，service 信息
PS：UserAgent, use python lib: httpagentparser
# Task 2
统计单个IP的 data_size, rtt, latency 时用一个CDF的10，20，50，80，90，99分位点的数据， 比如｛"data_size":[1,2,3,4,5,6]｝，其中［1,2,3,4,5,6] 分别对应data_size的CDF分布的10，20，50，80，90，99分位点
重传率和超时率只给出平均值

#文件说明
	＊ CdfQuantiles.py
		求数组的CDF分位数的函数 cdf_quantiles(arrays) 返回内置的分位数对应的数据

	＊ipdata.py
		数据类，用于存储每个ip的数据，包括 os，browser，service，data_size，rtt，retransrate，latency，timeout 
	
	＊ JsonPretty.py
		格式化每行一条的json数据，加上缩进，标准的‘，’和‘：’分隔符
		
	＊ MergeSesReq.py
		合并 session 和 request 文件的函数
		
	＊UAstat.py
		主程序，读取合并后的session和request文件，并依次处理每条数据
	
	＊ req.log
		UserAgent 无效信息的输出
		
	＊ session.request.json
		测试用输入文件
		
	＊ stat.json
		测试输出文件