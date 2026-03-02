select 
	`year` as "Anno pubblicazione",
	count(nome) "Numero giochi"
from games 
group by `year`
order by count(nome) desc
limit 10
;

select 
	publisher as "Publisher",
	count(nome) "Numero giochi"
from games 
group by publisher
order by count(nome) desc
limit 100
;


select 
	platform as "Platform",
	publisher as "Publisher",
	count(nome) "Numero giochi"
from games 
group by platform, publisher
order by  count(nome) desc, platform
limit 100
;

