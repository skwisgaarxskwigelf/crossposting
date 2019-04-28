from flask import flash, render_template
from .forms import ChannelsForm
from .. import db
from ..models import Channel
from . import crud_forms

#Channels Views


@crud_forms.route('/', methods=['GET', 'POST'])
def list_channels():
    """
    List all channels
    """
    channel = Chanel.query.all()
    try:
        return render_template('channels/channels.html',
                           channel, title="Channels")
    except:
        abort(404)


@crud_forms.route('/add', methods=['GET', 'POST'])
def add_channel():
    """
    Add a channel to the database
    """

    add_channel = True

    form = ChannelsForm()
    try:
        # add channel to the database
        db.session.add(channel)
        db.session.commit()
        flash('You have successfully added a new chanel.')
    except:
        # in case channel name already exists
        flash('Error: channel name already exists.')

    # redirect to channels page
    return redirect(url_for('crud_forms.list_channels'))

    #return render_template('admin/departments/department.html', action="Add",
    #                       add_department=add_department, form=form,
    #                       title="Add Department")


@crud_forms.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_channel(id):
    """
    Edit a channel
    """
    add_channel = False

    channel = Channel.query.get_or_404(id)
    form = ChannelsForm(obj=channel)
    #if form.validate_on_submit():
    channel.name = form.name.data
    #channel.description = form.description.data
    db.session.commit()
    flash('You have successfully edited the department.')

    # redirect to the channels page
    return redirect(url_for('crud_froms.list_channels'))

    #form.description.data = department.description
    form.name.data = channel.name
    return render_template('channels/channels.html', action="Edit",
                           add_channel=add_channel, form=form,
                           channel=channel, title="Edit Channel")


@crud_forms.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete_channel(id):
    """
    Delete a department from the database
    """
    channel = Channel.query.get_or_404(id)
    db.session.delete(channel)
    db.session.commit()
    flash('You have successfully deleted the channel.')

    # redirect to the departments page
    return redirect(url_for('crud_forms.list_channels'))

    return render_template(title="Delete Channel")
