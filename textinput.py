import os
import tempfile

def textinput(content=None, editor=None):
    if not editor:
        editor = os.environ.get('EDITOR','vim')
    tf = tempfile.NamedTemporaryFile()
    if content:
        tf.write(content)
        tf.seek(0)
    os.system("%s %s"%(editor, tf.name))
    data = tf.read()
    tf.close()
    if len(data) > 0 and data[-1] == "\n":
        data = data[:-1]
    return data

def viminput(content=None):
    return textinput(content, "vim")
