#-*-coding:utf-8-*-
import smtplib
from email.mime.text import MIMEText
from email.header import Header

#发送邮件告知一天的访问信息
def send_email(mess_list,id):
    see_num1 = 0;jifen1 = 0;paiming1 = 0; yc1 = 0; zz1=0;fy1 =0 ;pl1 = 0; m1 = ""
    see_num2 = 0;jifen2 = 0;paiming2 = 0; yc2 = 0; zz2=0;fy2 =0 ;pl2 = 0; m2 = ""
    for mess in mess_list:
        if mess["id"] == id -1:
            see_num1 = int(mess["me_mess"]["see_num"])
            jifen1 = int(mess["me_mess"]["jifen"])
            paiming1 = int(mess["me_mess"]["paiming"])
            yc1 = mess["me_mess"]["yuanchuang"]
            zz1 = mess["me_mess"]["zhuanzai"]
            fy1 = mess["me_mess"]["fanyi"]
            pl1 = mess["me_mess"]["pinglun"]
            m1 ="%s，总访问量：%s，积分：%s，博客排名：%s，原创文章：%s，转载文章：%s，翻译文章：%s，评论数：%s。" \
                % (mess["me_mess"]["time"],see_num1,jifen1,paiming1,yc1,zz1,fy1,pl1)
        elif mess["id"] == id:
            see_num2 = int(mess["me_mess"]["see_num"])
            jifen2 = int(mess["me_mess"]["jifen"])
            paiming2 = int(mess["me_mess"]["paiming"])
            yc2 = mess["me_mess"]["yuanchuang"]
            zz2 = mess["me_mess"]["zhuanzai"]
            fy2 = mess["me_mess"]["fanyi"]
            pl2 = mess["me_mess"]["pinglun"]
            m2 = "我是您的CSDN小助手，您的CSDN博客 http://blog.csdn.net/%s，\n%s，总访问量：%s，积分：%s，博客排名：%s，原创文章：%s，转载文章：%s，翻译文章：%s，评论数：%s。" \
              % (mess["me_mess"]["name"],mess["me_mess"]["time"],see_num2,jifen2,paiming2,yc2,zz2,fy2,pl2)
        else:
            message=""
    message = m2 +"\n"+ m1 + "\n相比昨天,访问量增长：%s,积分增长：%s, 排名增长：%s，原创文章数增长：%s，转载文章数增长：%s，翻译文章数增长：%s，评论数增长：%s" \
            %(str(see_num2-see_num1),str(jifen2-jifen1),str(paiming2-paiming1),str(yc2-yc1),str(zz2-zz1),str(fy2-fy1),str(pl2-pl1))

    # 第三方 SMTP 服务
    mail_host = "smtp.163.com"  # 设置服务器
    mail_user = "thinkgamer@163.com"  # 用户名
    mail_pass = "you_password"  # 口令

    sender = "thinkgamer@163.com"
    receive="thinkgamer@163.com"

    # 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
    message = MIMEText(message, 'plain', 'utf-8')
    message['From'] = Header("CSDN小助手", 'utf-8')
    message['To'] =  Header("", 'utf-8')

    subject = '【%s】CSDN博客访问信息统计' % mess["me_mess"]["time"]
    message['Subject'] = Header(subject, 'utf-8')

    try:
        smtpObj = smtplib.SMTP()
        smtpObj.connect(mail_host, 25)    # 25 为 SMTP 端口号
        smtpObj.login(mail_user,mail_pass)
        smtpObj.sendmail(sender, receive, message.as_string())
        print("邮件发送成功")
    except smtplib.SMTPException as e:
        print("Error: 无法发送邮件")
