# spider_on_3dm
##### 爬取3dm上的图片

# 想法
> 先获取网站上所有的网址信息
> 然后在对网址中的图片进行多线程下载
> * 为了保证速度,肯定要使用多线程的
>   * 那么问题是应该如何选择呢?
>   * **获取每个网址内的所有图片地址**
>   * **然后将这些地址放入到多线程中进行下载**
>   * 回去先看看书,确定如何多线程下载
> * 对于下载的网址,图片的log进行记录
> * 我要保证需要下载的东西必须下载完毕且不会重复下载
> * 写好每一个类,每一个方法
> * 学会单元测试
> * 代码符合pylint规范(虽然里面很多规则很麻烦)
> * 存储已获取的网址,每次启动程序,先对之前的网址进行下载,防止重复下载(?)
>   * 但是不确定是否有必要在这个程序里面这么做

# 步骤
> 1. 获取所有标题的网址
> 1. 获取标题内的图片网址
> 1. 根据图片网址内容,下载图片
> 突然发现3dm无需selenium~~直接使用requests和bs4就可以了

# 尝试
> 1. 尝试使用协程gevent --> 20181112,未成功,搁浅
> 1. 尝试使用thread+queue --> 这个比较熟悉,成功,不过未进行速度测试

# 未完成的工作
- [x] 添加logging.FileHandler,对程序进行监督
- [x] 将pic网址写入downloaded_urls.txt,防止下次重复下载
- [x] 为pic文件名称添加位置标识(页数_排名_pic文件名)
- [ ] 每天定时执行
- [ ] 在Debian(Raspberry)上部署
- [ ] 添加重连方法(?未确定)
- [x] 给程序添加StreamHandler,在控制台中了解程序状态(完成50%)
- [ ] 子进程报错问题,需要传递给主进程
