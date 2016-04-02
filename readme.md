#HappyDaily
提取出知乎日报中**瞎扯 · 如何正确地吐槽**栏目内容



#API

##某日数据
**http://news.at.zhihu.com/api/4/news/before/20110519**

样例：
>{"date":"20130519","stories":[{"images":["http:\/\/p2.zhimg.com\/96\/81\/9681ea63890cb65dab503bddfd7b7113_r.raw"],"type":0,"id":401,"ga_prefix":"051922","title":"学英语才是正经事儿"},{"images":["http:\/\/p1.zhimg.com\/88\/07\/8807985324e4cf2ae315eaf1bcfeb22a_r.raw"],"type":0,"id":396,"ga_prefix":"051919","title":"中老年人和外星人的区别"},{"images":["http:\/\/p3.zhimg.com\/b3\/a8\/b3a81050144a8684211f800982588ee3_r.raw"],"type":0,"id":395,"ga_prefix":"051918","title":"Windows 也能优雅地用？"},{"images":["http:\/\/p3.zhimg.com\/b0\/79\/b079691703f8926fec05febe8fd21f84_r.raw"],"type":0,"id":394,"ga_prefix":"051917","title":"Kindle 到底好在哪儿？"},{"images":["http:\/\/p1.zhimg.com\/4b\/fa\/4bfa1f143f01ff560893414cd64d9a97_r.raw"],"type":0,"id":390,"ga_prefix":"051915","title":"为什么光逃离不了黑洞"},{"images":["http:\/\/p2.zhimg.com\/ab\/19\/ab19235b36da52420b6654c03b8d259c_r.raw"],"type":0,"id":388,"ga_prefix":"051913","title":"小龙虾怎么做比较好吃"}]}

1. 其中日期以YYYYMMDD表示
2. 知乎日报第一天的内容在20130520

##封面图片
**http://news-at.zhihu.com/api/4/start-image/1080*1776**
样例：
>{"text":"Marcelo Quinan",
"img":"https:\/\/pic1.zhimg.com\/4e8411dfc1ecf83e415856a12e69c374.jpg"}

1. 支持320\*432, 480\*728, 720\*1184, 1080\*1776 四种分辨率


#Citation
1. [知乎](http://www.zhihu.com/) 所有原创内容均来自知乎
2. [ZhihuDailyPurify](https://github.com/izzyleung/ZhihuDailyPurify) API部分参考该项目
