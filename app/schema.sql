drop table if exists places;
create table places (
	id integer primary key not null,
	name text not null,
	description text not null,
	countyId integer not null,
	latitude real not null,
	longitude real not null,
	FOREIGN KEY(countyId) REFERENCES counties(id) 
);

drop table if exists counties;
create table counties (
	id integer primary key,
	name text not null,
        state text not null
);

drop table if exists activities;
create table activities (
	id integer primary key,
	name text not null
);

drop table if exists joinActPlace;
create table joinActPlace (
	id integer primary key not null,
	placeId integer not null,
	activityId integer not null,
	FOREIGN KEY(placeId) REFERENCES places(id),
	FOREIGN KEY(activityId) REFERENCES activities(id)
);
