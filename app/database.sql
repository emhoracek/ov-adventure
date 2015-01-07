INSERT INTO places VALUES(
    1, 
    'Wheeling Park', 
    'A city park.', 
    1, 
    40.0580813,-80.6671525);
INSERT INTO places VALUES(
    2, 
    'Schenley Pond', 
    'Paddle boats at Oglebay',
    2, 
    40.0977693,-80.6630598);
INSERT INTO places VALUES(
    3, 
    'Ski Slopes', 
    'Skiing at Oglebay', 
    3, 
    40.0953621,-80.660224);
INSERT INTO places VALUES (
	4,
	'Good Zoo',
	'Zoo and nature center', 
	4, 
	40.0914825,-80.6635319);
INSERT INTO places VALUES (
	5,
	'Wheeling Park pond',
	'Lots of birds.', 
	4, 
	40.0590549,-80.6696798);
INSERT INTO places VALUES (
	6,
	'Wheeling park ice skating',
	"It's almost outdoors.", 
	1, 
	40.0586479,-80.6668156);
INSERT INTO places VALUES (
	7,
	'Wheeling overlook',
	'Description of place', 
	10, 
	40.0799724,-80.7225178);
INSERT INTO places VALUES (
	8,
	'Waterfront Park',
	'Description of place', 
	7, 
	40.0672014,-80.724915);
INSERT INTO places VALUES (
	9, 
        'Tunnel Green', 
        'Shelters, roller hockey rink, baseball field, basketball courts.',
        7, 
        40.071452,-80.710526);
INSERT INTO places VALUES (
        10, 
        "Lewis Wetzel's cave", 
        "A cave near Tunnel Green", 
        7, 
        40.0727302,-80.71052);
INSERT INTO places VALUES (
	11,
	'Good Zoo',
	'Zoo and nature center', 
	1, 
	40.0814825,-80.5635319);
INSERT INTO places VALUES (
	12,
	'Wheeling Park pond',
	'Lots of birds.', 
	1, 
	40.0790549,-80.6196798);
INSERT INTO places VALUES (
	13,
	'Good Zoo',
	'Zoo and nature center', 
	7, 
	40.0914825,-80.6335319);
INSERT INTO places VALUES (
	14,
	'Wheeling Park pond',
	'Lots of birds.', 
	2, 
	40.0290549,-80.6896798);
INSERT INTO places VALUES (
	15,
	'Wheeling park ice skating',
	'Almost outdoors.', 
	1, 
	40.0886479,-80.6968156);

INSERT INTO activities VALUES(1, 'bicycle trails');
INSERT INTO activities VALUES(2, 'boating');
INSERT INTO activities VALUES(3, 'skiing');
INSERT INTO activities VALUES(4, 'skating');
INSERT INTO activities VALUES(5, 'hiking');
INSERT INTO activities VALUES(6, 'sailing');
INSERT INTO activities VALUES(7, 'fishing');
INSERT INTO activities VALUES(8, 'hunting');
INSERT INTO activities VALUES(9, 'swimming');

INSERT INTO joinActPlace VALUES(1, 1, 1);
INSERT INTO joinActPlace VALUES(2, 2, 1);
INSERT INTO joinActPlace VALUES(3, 2, 2);
INSERT INTO joinActPlace VALUES(4, 1, 2);
INSERT INTO joinActPlace VALUES(5, 1, 3);
INSERT INTO joinActPlace VALUES(6, 2, 3);
INSERT INTO joinActPlace VALUES(7, 3, 3);
INSERT INTO joinActPlace VALUES(8, 1, 4);
INSERT INTO joinActPlace VALUES(9, 7, 4);
INSERT INTO joinActPlace VALUES(10, 1, 5);
INSERT INTO joinActPlace VALUES(11, 1, 6);
INSERT INTO joinActPlace VALUES(12, 1, 7);
INSERT INTO joinActPlace VALUES(13, 1, 8);
INSERT INTO joinActPlace VALUES(14, 9, 8);

