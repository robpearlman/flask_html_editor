#/project/__init__.py

#################
#### imports ####
#################
from flask import Flask, flash, redirect, render_template, g, session, url_for, request, make_response, send_file
from flask_wtf import Form
from wtforms import TextField, SelectField, SubmitField
from cktext import CKTextAreaField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config.from_pyfile('_config.py')

################
#### routes ####
################


startfile = " <!DOCTYPE html><html><head><meta http-equiv='Content-Type' content='text/html; charset=utf-8'><meta name='viewport' content='width=device-width; initial-scale=1, maximum-scale=1'><link href='normalize.css' rel='stylesheet' type='text/css' /><link href='skeleton.css' rel='stylesheet' type='text/css' /><link href='swipebox.css' rel='stylesheet' type='text/css' /><script type='text/javascript' src='jquery-2.2.3.min.js'></script><script src='jquery.swipebox.js'></script> </head><body><div class='container'><div id='content'> "
endfile = " </div><br><br></div><script>function _c(e){return document.getElementsByTagName(e)}for(i = 0; i < _c('img').length; i++){console.log(_c('img')[i].parentNode.classList.contains('swipebox'));if(_c('img')[i].parentNode.classList.contains('swipebox') === true){console.log('s');}else {var hs = _c('img')[i].getAttribute('src');var ssa = document.createElement('a');ssa.href = hs; ssa.className = 'swipebox';if(_c('img')[i].classList != undefined){if(_c('img')[i].classList.contains('backup_picture') === false){_c('img')[i].className = 'backup_picture';}}else {_c('img')[i].className = 'backup_picture';}_c('img')[i].parentNode.insertBefore(ssa,_c('img')[i]);ssa.appendChild(_c('img')[i]);}};( function( $ ) {$( '.swipebox' ).swipebox({hideCloseButtonOnMobile : false});$('.backup_picture').error(function(){$(this).attr('src', 'image_error.png');});} )( jQuery );</script></body></html> "

class EditContentCKEditorForm(Form):
    # add heading/filename box
    ckeditor = CKTextAreaField('Item Details', default="", validators=[DataRequired(message=(u'Please enter some content'))])
    savename = TextField('File Name', default="", validators=[DataRequired()])
    submit1 = SubmitField('submit')

class LoadFileForm(Form):    
    filechoices = SelectField('Files Available', validators=[DataRequired()])
    submit2 = SubmitField('load file')


@app.route('/', methods=['GET', 'POST'])
@app.route('/<string:filetoload>', methods=['GET', 'POST'])
# simply renders the main page
def index(filetoload=None):
    # initialise forms
    form = EditContentCKEditorForm(request.form)
    loadfilesform = LoadFileForm(request.form)
    # if filetoload is true, then im trying to load a file
    if filetoload:
        form.savename.data = filetoload[:-5]
        filetoload = 'HTML/' + filetoload
        file = open(filetoload, 'r')
        content = file.read()
        content = content[len(startfile):]
        content = content[:-len(endfile)]
        form.ckeditor.data = content
    # now generate a selectfield's data points by traversing the HTML Directory and filtering for HTML files
    from os import listdir
    from os.path import isfile, join
    onlyfiles = [f for f in listdir('HTML/') if isfile(join('HTML/', f))]
    onlyfiles = [f for f in onlyfiles if f[-4:] == 'html']
    loadfilesform.filechoices.choices = [(p, p) for p in onlyfiles]

    if request.method == 'POST':
        # Put in write HTML file stuff here, but this is probably slightly out of place now
        if form.submit1.data:
            save_name = 'HTML/' + form.savename.data + '.html'
            with open(save_name, 'w') as save_file:
                data_construct = str(startfile + '\n\n\n' + form.ckeditor.data + '\n\n\n' + endfile)
                save_file.write(data_construct)
            flash('Item was updated and saved as ' + form.savename.data)
        elif loadfilesform.submit2.data:
            filetoload = loadfilesform.filechoices.data
            print filetoload
            flash('Loaded file ' + filetoload)
            return redirect(url_for('index', filetoload=filetoload))
    #print content.data
    return render_template("index.html", form=form, loadfilesform=loadfilesform, content=content)








