# pega-sql-converter
Tiny tool for converting SQL queries from Pega Tracer

# Usage
Add to first text input SQL from Tracer:
```SQL
SELECT "PC0".PYCLASSNAME AS "pyClassName" , "PC0".PXINSNAME AS "pxInsName" , "PC0".PYRULESETVERSION AS "pyRuleSetVersion" , "PC0".PZINSKEY AS "pzInsKey" , "PC0".PYRULEAVAILABLE AS "pyRuleAvailable" , "PC0".PYRULESET AS "pyRuleSet" , "PC0".PYCIRCUMSTANCETYPE AS "pyCircumstanceType" , "PC0".PYCIRCUMSTANCEPROP AS "pyCircumstanceProp" , "PC0".PYCIRCUMSTANCEDATEPROP AS "pyCircumstanceDateProp" , "PC0".PYCIRCUMSTANCEDATE AS "pyCircumstanceDate" , "PC0".PYCIRCUMSTANCEVAL AS "pyCircumstanceVal" , "PC0".PYRULESTARTS AS "pyRuleStarts" , "PC0".PYRULEENDS AS "pyRuleEnds" FROM PRPC.pr4_rule "PC0" WHERE ( "PC0".PYCLASSNAME = ? AND "PC0".PXINSNAME = ? AND ( "PC0".PYRULESET = ? OR "PC0".PYRULESET = ? ) AND "PC0".PXOBJCLASS = ? ) ORDER BY 3 DESC
```
Add to second text input SQL Inserts from Tracer:
```
<System-User-Dashboard> <SYSTEM-USER-DASHBOARD!PYDEFAUTUSERDASHBOARD> <Virusmater> <Pega-EndUserUI> <Rule-Obj-Model>
```
Press Generate button and grab results from last text input:
```SQL
SELECT "PC0".PYCLASSNAME AS "pyClassName" , "PC0".PXINSNAME AS "pxInsName" , "PC0".PYRULESETVERSION AS "pyRuleSetVersion" , "PC0".PZINSKEY AS "pzInsKey" , "PC0".PYRULEAVAILABLE AS "pyRuleAvailable" , "PC0".PYRULESET AS "pyRuleSet" , "PC0".PYCIRCUMSTANCETYPE AS "pyCircumstanceType" , "PC0".PYCIRCUMSTANCEPROP AS "pyCircumstanceProp" , "PC0".PYCIRCUMSTANCEDATEPROP AS "pyCircumstanceDateProp" , "PC0".PYCIRCUMSTANCEDATE AS "pyCircumstanceDate" , "PC0".PYCIRCUMSTANCEVAL AS "pyCircumstanceVal" , "PC0".PYRULESTARTS AS "pyRuleStarts" , "PC0".PYRULEENDS AS "pyRuleEnds" FROM PRPC.pr4_rule "PC0" WHERE ( "PC0".PYCLASSNAME = 'System-User-Dashboard' AND "PC0".PXINSNAME = 'SYSTEM-USER-DASHBOARD!PYDEFAUTUSERDASHBOARD' AND ( "PC0".PYRULESET = 'Virusmater' OR "PC0".PYRULESET = 'Pega-EndUserUI' ) AND "PC0".PXOBJCLASS = 'Rule-Obj-Model' ) ORDER BY 3 DESC
```