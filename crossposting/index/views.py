from flask import abort, flash, redirect, render_template, url_for
from . import index
from .forms import ChannelsForm
from .. import db
from ..models import Channel


@index.route('/', methods=['GET', 'POST'])
def list_channels():
    """
    List all channels
    """
    channels = Channel.query.all()

    try:
        return render_template('channels/channels.html', channels=channels, title="Channels")
    except:
        abort(404)


@index.route('/add', methods=['GET', 'POST'])
def add_channel():
    """
    Add a channel to the database
    """
    add_channel = True

    form = ChannelsForm()
    if form.validate_on_submit():
        channels = Channel(name=form.name.data.strip(), channel_id=form.channel_id.data.strip(),
                           is_active=form.is_active.data)
        try:
            # add channel to the database
            db.session.add(channels)
            db.session.commit()
            flash('You have successfully added a new chanel.')
        except:
            flash('Error: channel name already exists.')
        return redirect(url_for('index.list_channels'))

    return render_template('channels/channel.html', action="Add", add_channel=add_channel,
                           form=form, title="Add Channel")


@index.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_channel(id):
    """
    Edit a channel
    """
    add_channel = False

    channels = Channel.query.get_or_404(id)
    form = ChannelsForm(obj=channels)
    if form.validate_on_submit():
        channels.name = form.name.data
        channels.chat_id = form.chat_id.data
        channels.is_active = form.is_active.data
        db.session.commit()
        flash('You have successfully edited the channel.')

        # redirect to the channels page
        return redirect(url_for('index.list_channels'))

    form.name.data = channels.name
    return render_template('channels/channel.html', action="Edit",
                           add_channel=add_channel, form=form,
                           channels=channels, title="Edit Channel")


@index.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete_channel(id):
    """
    Delete a department from the database
    """
    channels = Channel.query.get_or_404(id)
    db.session.delete(channels)
    db.session.commit()
    flash('You have successfully deleted the channel.')

    # redirect to the departments page
    return redirect(url_for('index.list_channels'))

    return render_template(title="Delete Channel")
