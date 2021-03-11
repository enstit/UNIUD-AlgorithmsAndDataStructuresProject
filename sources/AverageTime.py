growth_PN2 = []
for s in strings:
	i=0
   	t_passed = 0
	
	while(t_passed<=t_min):
		start=t.time()
		PeriodNaive(s)
		end=t.time()
		i=i+1
		t_passed+=end-start
		
   		
	growth_PN2.append(t_passed/i)
