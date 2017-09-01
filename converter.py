import re

def convert(sqlText, sqlInserts):
    rex = re.compile("^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d*")
    start = sqlInserts.find('<')
    while start >= 0:
        end = sqlInserts.find('>', start)
        if (end == -1):
            break
        insert = sqlInserts[start + 1:end]
        # if date
        if rex.match(insert):
            insert = 'TO_DATE(\'' + insert[0: 19] + '\', \'YYYY-MM-DD HH24:MI:SS\')'
        else:
            # if is NULL that surrounded with double brackets
            if insert[0] == "<":
                insert = insert.replace('<', '')
                end += 1
            # else surround with quotes
            else:
                insert = '\'' + insert + '\''
        if '&' in insert:
            insert = insert.replace('&', '\'|| chr(38) || \'')
        sqlText = sqlText.replace('?', insert, 1)
        start = end + 2
    return sqlText