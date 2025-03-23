-- From the discussion comments:

with ord as (
Select * from Orders where YEAR(order_date) = '2019'
)
Select U.user_id as buyer_id, U.join_date, 
    SUM(CASE WHEN order_date is not null then 1 ELSE 0 END) as orders_in_2019 from Users U
left join ord O on U.user_id = O.buyer_id 
group by U.user_id , U.join_date