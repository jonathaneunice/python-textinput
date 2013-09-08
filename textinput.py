import os
import tempfile

def textinput(content=None, editor=None):
    if not editor:
        editor = os.environ.get('EDITOR','vim')
    tf = tempfile.NamedTemporaryFile(delete=False)
    if content:
        tf.write(content)
    tf.close()
    os.system("%s %s"%(editor, tf.name))
    tf = open(tf.name, "rb")
    data = tf.read()
    tf.close()
    os.remove(tf.name)
    if len(data) > 0 and data[-1] == "\n":
        data = data[:-1]
    return data

def viminput(content=None):
    return textinput(content, "vim")
