select * from category;

select venuename 
from venue 
where venuestate='DC' 
order by venuename; 

select eventname, SUM(qtysold) as total_attendance 
from sales 
inner join event on sales.eventid = event.eventid
group by eventname
order by total_attendance desc limit 10;

SELECT eventname, starttime
FROM Event
INNER JOIN Date ON Event.dateid = Date.dateid
WHERE caldate = '2008-08-21';


select sellerid, SUM(numtickets) as total_tickets_listed
from listing
group by sellerid
order by total_tickets_listed desc
limit 1;

Select catname, count(event.eventid) as num_events
from category
left join event on category.catid = event.catid
group by catname;

select sum(sales.commission) as total_commission
from sales
inner join event on sales.eventid = event.eventid
inner join venue on event.venueid = venue.venueid
where venue.venuecity = 'Kansas City';

select catname, avg(pricepaid/qtysold) as avg_ticket_price
from category
Inner join event on category.catid = event.catid
inner join sales on event.eventid = sales.eventid
group by catname;

with eventsales as 
(
	select category.catid,
		count(sales.salesid) as total_sales,
		avg(sales.commission) as avg_commission
	from event
	inner join sales on event.eventid = sales.eventid
	inner join category on event.catid = category.catid
	group by category.catid 
)
select category.catname,
	eventsales.total_sales,
	eventsales.avg_commission
from category
inner join eventsales on category.catid = eventsales.catid;


create view high_revenue_events as
select eventid, sum(pricepaid) as total_revenue
from sales
group by eventid
having sum(pricepaid) > 50000;
select * from high_revenue_events;


select dateid, 
	sum(qtysold) as total_sales, 
	lag(sum(qtysold)) over (order by dateid) as previous_day_total_sales
from sales 
group by dateid 
order by dateid;

