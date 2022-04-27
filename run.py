import itchat
from itchat.content import *
from .tuling import dm_to_tuling

@itchat.msg_register([TEXT, MAP, CARD, NOTE, SHARING])
def text_reply(msg):
    if msg.type == "TEXT":
        resp = dm_to_tuling(msg.text)
        msg.user.send('%s' % (resp))
    msg.user.send('%s: %s' % (msg.type, msg.text))

@itchat.msg_register([PICTURE, RECORDING, ATTACHMENT, VIDEO])
def download_files(msg):
    msg.download(msg.fileName)
    typeSymbol = {
        PICTURE: 'img',
        VIDEO: 'vid', }.get(msg.type, 'fil')
    return '@%s@%s' % (typeSymbol, msg.fileName)

@itchat.msg_register(FRIENDS)
def add_friend(msg):
    msg.user.verify()
    msg.user.send('Nice to meet you!')

@itchat.msg_register([TEXT, PICTURE], isGroupChat=True)
def text_reply(msg):
    if msg.isAt:
        if msg.type == "TEXT":
            resp = dm_to_tuling(msg.text)
            msg.user.send('%s' % (resp))
            msg.user.send(u'@%s\u2005 %s' % (
                msg.actualNickName, resp))
        to_user = itchat.search_friends(nickName="徐楠(燕斌)")
        for user in to_user:
            user.send(msg.text)
            

itchat.auto_login(True, enableCmdQR=2)
itchat.run(True)
