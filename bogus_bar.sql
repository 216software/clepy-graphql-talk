create table musicians (
    musician_id integer primary key,
    name citext not null,
    description text,
    website_url text
);

create table events (
    event_date date not null,
    musician_id integer not null references musicians (musician_id),
    primary key (event_date, musician_id)
);

insert into musicians
(musician_id, name, website_url)
values
(1, 'Black Death', null),
(2, 'Johnny LaRock', 'http://www.johnnylarock.com/'),
(3, 'Sarah Arafat', 'https://saraharafat.bandcamp.com/');

-- Sarah Arafat plays the next three Tuesdays
insert into events
(event_date, musician_id)
values
('2020-05-12', 3),
('2020-05-19', 3),
('2020-05-26', 3);

-- Black Death is playing on Friday and Saturday night
insert into events
(event_date, musician_id)
values
('2020-05-15', 1),
('2020-05-16', 1);


-- Black Death just renamed themselves, and got a facebook page.
update musicians
set name = 'Black Death Resurrected',
website_url = 'https://www.facebook.com/BlackDeathResurrected/'
where musician_id = 1;

-- List the schedule.
select events.event_date, musicians.name
from events
join musicians
on events.musician_id = musicians.musician_id
where event_date > current_timestamp
and event_date < current_timestamp + interval '30 days'
order by event_date;

/*

+------------+-------------------------+
| event_date |          name           |
+------------+-------------------------+
| 2020-05-12 | Sarah Arafat            |
| 2020-05-15 | Black Death Resurrected |
| 2020-05-16 | Black Death Resurrected |
| 2020-05-19 | Sarah Arafat            |
| 2020-05-26 | Sarah Arafat            |
+------------+-------------------------+

*/

create view upcoming_shows
as
select events.event_date, musicians.name, musicians.website_url
from events
join musicians
on events.musician_id = musicians.musician_id
where event_date > current_timestamp
and event_date < current_timestamp + interval '30 days'
order by event_date
;

/*

+------------+-------------------------+-------------------------------------------------+
| event_date |          name           |                   website_url                   |
+------------+-------------------------+-------------------------------------------------+
| 2020-05-12 | Sarah Arafat            | https://saraharafat.bandcamp.com/               |
| 2020-05-15 | Black Death Resurrected | https://www.facebook.com/BlackDeathResurrected/ |
| 2020-05-16 | Black Death Resurrected | https://www.facebook.com/BlackDeathResurrected/ |
| 2020-05-19 | Sarah Arafat            | https://saraharafat.bandcamp.com/               |
| 2020-05-26 | Sarah Arafat            | https://saraharafat.bandcamp.com/               |
+------------+-------------------------+-------------------------------------------------+

*/

-- Pretend somebody calls and asks "Hey when is Johnny LaRock playing?"
select events.event_date
from events
join musicians
on events.musician_id = musicians.musician_id
where musicians.name = 'Johnny LaRock'
and events.event_date > current_timestamp
order by events.event_date;

