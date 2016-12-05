# -*- coding: utf-8 -*-

from flask import render_template, request, flash, redirect, url_for,current_app,abort
from . import main
from .. import db
from ..models import News
from flask_babel import gettext as _

@main.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404




@main.route('/')
def index():
#    posts=News.query.all()
    page_index = request.args.get('page', 1, type=int)
    query = News.query.order_by(News.id.desc())
    pagination = query.paginate(page_index, per_page=3, error_out=False)
    posts = pagination.items
    return render_template('index.html',
                           page_list=posts,
                           pagination=pagination)

'''
@main.route('/add/<int:id>', methods=['GET', 'POST'])
def add(request):
    try:
        content = request.GET.get("page", None)
        print(content)
        if len(content) > 0:
            obj = News.objects.create(Text=content)
            if obj:
                return redirect(url_for("/blog/index"))
    except Exception as e:
        print e
    return render_template(request, "message.html", {"message": u"待办事项添加失败"})


@main.route('/edit', methods=['GET', 'POST'])
@main.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id=0):
    form = PostForm()

    if id == 0:
  #      post = Post(author=current_user)
        post =Post(author_id=current_user.id)
    else:
        post = Post.query.get_or_404(id)

    if form.validate_on_submit():
        post.body = form.body.data
        post.title = form.title.data

        db.session.add(post)
        db.session.commit()

        return redirect(url_for('.post', id=post.id))

    form.title.data = post.title
    form.body.data = post.body

    title = _(u'添加新文章')
    if id > 0:
        title = _(u'编辑 - %(title)', title=post.title)
'''
@main.route('/shoutdown')
def shutdown():
    if not current_app.testing:
        abort(404)

    shoutdown = request.environ.get('werkzeug.server.shutdown')
    if not shoutdown:
        abort(500)

    shoutdown()
    return u'正在关闭服务端进程...'
