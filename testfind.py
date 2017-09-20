line='<ComponentElement ID="02" Name="5004 Monetary Amount"  Alias="_02_5004_Monetary_Amount" Req="O" MaxUse="1" MinLength="1" MaxLength="35" Type="N" />'

loc=line.find('Name=',0,99)
print(loc)
loc=loc+6
print(loc)
x=line[loc:loc+4]
print(x)
