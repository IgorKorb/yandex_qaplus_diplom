SELECT "Couriers".login, COUNT(*) as numbers_of_orders
FROM "Couriers"
JOIN "Orders" ON "Couriers".id="Orders"."courierId"
WHERE "Orders"."inDelivery" = true
GROUP BY "Couriers".login
ORDER BY "Couriers".login;


SELECT "Orders".track,
CASE
WHEN "Orders".finished = true THEN 2
WHEN "Orders".cancelled = true THEN -1
WHEN "Orders"."inDelivery" = true THEN 1
ELSE 0
END AS status
FROM "Orders";

## Нас не учили присоединять БД к pycharm, но я очень пытался сделать это самостоятельно, но к базам тренажёра
## подключиться не вышло. В каком виде нужно сдавать работу с базами sql (задание 1 и 2?).