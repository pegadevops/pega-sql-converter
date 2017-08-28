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
        if '&' in insert:
            insert = insert.replace('&', '\'|| chr(38) || \'')
        sqlText = sqlText.replace('?', insert, 1)
        start = end + 2
    return sqlText
