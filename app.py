from flask import Flask, render_template
from datetime import datetime
import foo




app = Flask(__name__)

@app.route('/')
def homepage():
    the_time = datetime.now().strftime("%A, %d, %b %Y %l:%M %p")
    the_quakes = foo.get_quake_data()

    for q in the_quakes:
        q['latlng'] = q['latitude'] + ',' + q['longitude']
        q['gmap_url'] = foo.prepare_static_gmap_url(q['latlng'],
                widthheight='200x200',
                zoom=5)

    locs = [q['latlng'] for q in the_quakes]
    world_map_url = foo.prepare_static_gmap_url(locs, widthheight='800x300')

    html = render_template('homepage.html',
            time=the_time, quakes=the_quakes,
            world_map_url=world_map_url)
    return html


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)


