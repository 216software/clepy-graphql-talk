begin;

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
(musician_id, name)
values
(1, 'Black Death'),
(2, 'Johnny LaRock'),
(3, 'Sarah Arafat');


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

-- List the schedule.
select events.event_date, musicians.name
from events
join musicians
on events.musician_id = musicians.musician_id
order by event_date;

-- Black Death just renamed themselves!
update musicians
set name = 'Black Death Resurrected'
where musician_id = 1;

-- List the schedule.
select events.event_date, musicians.name
from events
join musicians
on events.musician_id = musicians.musician_id
order by event_date;


rollback;

