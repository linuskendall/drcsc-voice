import MySQLdb
conn = MySQLdb.connect(host='127.0.0.1', unix_socket='/tmp/mysql.sock', user='root', passwd='default', db='drcsc') 
cur = conn.cursor() 

cur.execute("SELECT COUNT(*) FROM messages WHERE replyto = -1")
questions = cur.fetchone()

cur.execute("SELECT COUNT(*) FROM messages AS q INNER JOIN messages AS a ON a.replyto = q.id WHERE q.replyto = -1");
answered = cur.fetchone()

cur.execute("SELECT COUNT(*) FROM messages WHERE replyto=-1 AND id NOT IN (select replyto from messages where replyto != -1)");
unanswered = cur.fetchone()

cur.execute("SELECT COUNT(*) FROM messages WHERE replyto != -1");
answers = cur.fetchone()

cur.execute("SELECT MIN(dt) FROM messages WHERE replyto=-1 AND id NOT IN (select replyto from messages where replyto != -1)");
oldest_unanswered = cur.fetchone()

cur.execute("SELECT MAX(q.dt) FROM messages AS q INNER JOIN messages AS a ON a.replyto = q.id WHERE q.replyto = -1");
newest_answered = cur.fetchone()

cur.execute("SELECT MAX(a.dt) FROM messages AS q INNER JOIN messages AS a ON a.replyto = q.id WHERE q.replyto = -1");
latest_answer = cur.fetchone()

cur.execute("SELECT COUNT(*) FROM users WHERE NOT blocked");
unique_users = cur.fetchone()

cur.execute("SELECT a.dt,q.dt,DATEDIFF(a.dt,q.dt) FROM messages AS a INNER JOIN messages AS q ON q.id = a.replyto GROUP BY a.replyto HAVING a.dt = MIN(a.dt)");
average_time = cur.fetchone()[2]

cur.execute("SELECT COUNT(distinct user_id) FROM messages WHERE dt > (NOW() - INTERVAL 7 DAY)")
weekly_active_users = cur.fetchone()

cur.execute("SELECT COUNT(DISTINCT user_id) FROM messages WHERE dt > (NOW() - INTERVAL 1 MONTH)")
monthly_active_users = cur.fetchone()

cur.execute("SELECT COUNT(DISTINCT user_id) FROM log WHERE dt > (NOW() - INTERVAL 7 DAY)")
weekly_users = cur.fetchone()

cur.execute("SELECT COUNT(DISTINCT user_id) FROM log WHERE dt > (NOW() - INTERVAL 1 MONTH)")
monthly_users = cur.fetchone()

cur.execute("SELECT COUNT(DISTINCT callid) FROM log WHERE callerid != 100")
calls = cur.fetchone()

cur.execute("SELECT COUNT(DISTINCT callid) FROM log WHERE dt > (NOW() - INTERVAL 7 DAY)")
weekly_calls = cur.fetchone()

cur.execute("SELECT COUNT(DISTINCT callid) FROM log WHERE dt > (NOW() - INTERVAL 1 MONTH)")
monthly_calls = cur.fetchone()

print "Total questions: %s" % questions
print "- Answered questions: %s" % answered
print "- Unaswered questions: %s" % unanswered

print "Total answers: %s" % answers
print "- Average answers per query: %f" % (answers[0] / answered[0])

print "Average time taken to answer a query: %s days" % average_time
print "- Oldest unanswered query: %s" % oldest_unanswered
print "- Newest answered query: %s" % newest_answered
print "- Latest answer: %s" % latest_answer

print "Total users: %s" % unique_users
print "- Active this week: %s" % weekly_active_users
print "- Active this month: %s" % monthly_active_users
print "- Called this week: %s" % weekly_users
print "- Called this month: %s" % monthly_users 

print "Total calls: %s" % calls
print "- Calls this week: %s" % weekly_calls
print "- Calls this month: %s" % monthly_calls

cur.close() 
conn.close() 
