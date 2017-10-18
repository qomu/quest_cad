import vk
import links
import time

session = vk.Session(access_token=links.token)
api=vk.API(session)
with open('main.py', 'r') as text_file:
    s=text_file.read()
count = api.wall.get(owner_id=-139207940)[0]
done = 0
quest=[]
portion_len=0
while done<count-1:
    time.sleep(0.5)
    portion = api.wall.get(owner_id=-139207940, count=100, offset=done)[1:]
    for i in range(1, 101):
        try:
            if '#notequest1' in portion[i]['text']:
                quest.append(portion[i]['text'])
                # print('post appended')
            portion_len+=1
            # print('line checked, {} messages so far'.format(portion_len))
        except UnicodeEncodeError:
            pass
        except IndexError:
            break
    done+=portion_len
    portion_len=0
with open('log.html','w') as log:
    quest.reverse()
    log.write('<html>\n\t<head></head>\n\t<body>\n')
    for item in quest:
        log.write('-'*100+'<br>')
        log.write(item)
        log.write('<br><br>')
    log.write('\n\t</body>\n</html>')
