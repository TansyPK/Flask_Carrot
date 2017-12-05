# -*- coding: utf-8 -*-
import os
import time
import hashlib

from flask_uploads import UploadSet, IMAGES
from flask_login import login_required

"""
    Author: Grey Li
    Blog: http://greyli.com
    Email: withlihui@gmail.com
    Git repository: https://github.com/greyli/image-wall
    This work based on impress.js which can be found at https://github.com/impress/impress.js
"""

from flask import request, render_template, redirect, url_for,Blueprint
from Blog.photos.generator import ImageWall
#蓝图
photos_api = Blueprint('photos_api',__name__)
#上传对象
photos = UploadSet('photos', IMAGES)

@photos_api.route('/upload', methods=['GET', 'POST'])
@login_required
def upload():
    if request.method == 'POST' and 'photo' in request.files:
        amount = len(request.files.getlist('photo'))
        if amount in range(10, 101):
            for num, img in enumerate(request.files.getlist('photo')):
                filename = 'Koiphotos' + str(num)
                photos.save(img, name='Koiphotos' + '/' + filename + '.')
            return redirect(url_for('photos_api.image_wall'))
    return render_template('Koiphotos_templates/index.html')


@photos_api.route('/image_wall')
@login_required
def image_wall():
    wall = ImageWall('Koiphotos')
    count = len(os.listdir(wall.photo_folder))
    if count!=0:
        images = wall.create()
        overview = wall.overview()
        return render_template('Koiphotos_templates/wall.html', overview=overview, images=images)
    else:
        return redirect(url_for('photos_api.upload'))