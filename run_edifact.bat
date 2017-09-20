ECHO %1
SET IW_LIB=C:\iway8\lib
SET DRIVER_LIB=C:\iway8\lib
SET sef_dir=C:\SVN\iway8\svn\iway8schemas\trunk\ebix\edifact\EDIFACT_%%TOKEN%%\src\main\resources\1.0\%%TOKEN%%\sef
SET dic_dir=C:\SVN\iway8\svn\iway8schemas\trunk\ebix\edifact\EDIFACT_%%TOKEN%%\src\main\resources\1.0\%%TOKEN%%\dictionaries
SET header_file=C:\SVN\iway8\svn\iway8schemas\trunk\ebix\edifact\EDIFACT_%%TOKEN%%\src\main\resources\1.0\%%TOKEN%%\dictionaries\FACTHeader.dic
SET CP=%IW_LIB%\iway61.jar;%IW_LIB%\iwutil.jar;%IW_LIB%\iwtranse.jar;%DRIVER_LIB%\antlr-2.7.6.jar;%IW_LIB%\iwtransc.jar;%IW_LIB%\jakarta-regexp-1.2.jar;%IW_LIB%\iwxmldb.jar;%IW_LIB%\iwaf.jar
REM "C:\Program Files\Java\jre1.8.0_111\bin\java.exe" -Xmx512m -cp %CP% com.ibi.sef.SEFParser -dir %sef_dir% -header %header_file% -set complex -p -type FACT
"C:\Program Files\Java\jre1.8.0_111\bin\java.exe" -Xmx512m -cp %CP% com.ibi.sef.GeneratorXSD -dir %dic_dir% -header %header_file% -optimprefix schemas
svn commit -m "[[Jira(ATE-197)]] %%TOKEN%% looping" C:\SVN\iway8\svn\iway8schemas\trunk\ebix\edifact\EDIFACT_%%TOKEN%%\src\main\resources\1.0\%%TOKEN%%\dictionaries
svn commit -m "[[Jira(ATE-197)]] %%TOKEN%% looping" C:\SVN\iway8\svn\iway8schemas\trunk\ebix\edifact\EDIFACT_%%TOKEN%%\src\main\resources\1.0\%%TOKEN%%\schemas
