SELECT user_id, name, mail
FROM Users
WHERE mail LIKE '%@leetcode.com'
AND left(mail, len(mail)-13) LIKE '[A-Za-z]%'
and left(mail,LEN(mail) - 13) NOT LIKE '%[^A-Za-z0-9._-]%'