from flask import g

# id is not included so that sqlite will auto-increment the primary key
add_new_place = ('insert into places (name, description, ' +
                 'countyId, latitude, longitude) ' +
                 'values (?, ?, ? , ?, ?)')

add_new_user = 'insert into users (username, password) values (?, ?)'
