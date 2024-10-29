
    
    

select
     as unique_field,
    count(*) as n_records

from DEV.ANALYTICS.session_summary
where  is not null
group by 
having count(*) > 1


