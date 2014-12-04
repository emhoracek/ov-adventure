from flask import g

add_new_place = ('insert into places (id, name, description, ' +
                 'areaId, latitude, longitude) ' +
                 'values (?, ?, ?, ? ,?,?)')
