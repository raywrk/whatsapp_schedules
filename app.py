import pywhatkit as pwk
import pandas as pd
import time
import psycopg2

def whatsapp_send():
  db_connection = psycopg2.connect(host='ec2-54-235-98-1.compute-1.amazonaws.com', database='da9l8k9c6ulbd5',
                                  user='lcmulsicvhazdl', password='0101b23af78c44e6bf095833662077d9909afdc669962f0fd8b7ef593916fd91', port='5432')
  db_cursor = db_connection.cursor()
  db_cursor.execute(f'''
      SELECT 
            c.id,
            c.phone_wpp,
            c.group_wpp,
            c.message,
            c.image_path,
            c.data_send,
            c.hour_send,
            c.minute_send
      FROM contacts c
      WHERE c.data_send = to_char(now(), 'YYYY-MM-DD'::text)::date
      ORDER BY c.hour_send, c.minute_send;
        ''')
  result = db_cursor.fetchall()
  db_connection.close()

  columns = ['id', 'phone_wpp', 'group_wpp', 'message', 'image_path', 'data_send', 'hour_send', 'minute_send']
  df = pd.DataFrame(data=result, columns=columns)

  print(df)

  for i, mensagem in enumerate(df['message']):
      numero = df.loc[i, 'phone_wpp']
      hora = df.loc[i, 'hour_send']
      minuto = df.loc[i, 'minute_send']
      imagem = df.loc[i, 'image_path']

      if 
      pwk.sendwhatmsg(numero, mensagem, hora, minuto)
      time.sleep(5)
      pwk.sendwhats_image(numero, imagem)
      pwk.sendwhatmsg_to_group('CAgkl463j9cABgLi545hN1', 'Hey All!', 0, 0)
      
whatsapp_send()