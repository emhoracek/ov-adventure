from flask import g

add_new_place = ('insert into places (id, name, description, ' +
                 'countyId, latitude, longitude) ' +
                 'values (?, ?, ?, ? ,?,?)')

add_new_user = 'insert into users (username, password) values (?, ?)'
