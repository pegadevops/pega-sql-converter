def convert(sqlText, sqlInserts):
    start = sqlInserts.find('<')
    while start >= 0:
        end = sqlInserts.find('>', start)
        if (end == -1):
            break
        insert = sqlInserts[start + 1:end]
        # if is NULL that surrounded with double brackets
        if insert[0] == "<":
            insert = insert.replace('<', '')
        # else surround with quotes
        else:
            insert = '\'' + insert + '\''
        sqlText = sqlText.replace('?', insert, 1)
        start = end + 2
    return sqlText