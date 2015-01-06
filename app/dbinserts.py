from flask import g

add_new_place = ('insert into places (id, name, description, ' +
                 'countyId, latitude, longitude) ' +
                 'values (?, ?, ?, ? ,?,?)')
