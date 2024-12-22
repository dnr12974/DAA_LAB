def weighted_interval_scheduling(jobs):
    jobs=sorted(jobs,key=lambda x:x[1])
    n=len(jobs)
    M=[0]*(n+1)
    V=[0]+[job[2] for job in jobs]
    selected_jobs=[]
    def p(j):
        for i in range(j-1,0,-1):
            if jobs[i-1][1]<=jobs[j-1][0]:
                return i
        return 0
    for j in range(1,n+1):
        M[j]=max(V[j]+M[p(j)],M[j-1])
    j=n
    while j>0:
        if V[j]+M[p(j)]>M[j-1]:
            selected_jobs.append(jobs[j-1])
            j=p(j)
        else:
            j=j-1
    selected_jobs.reverse()
    return M[n],selected_jobs
def get_jobs_from_user():
    jobs=[]
    number_of_jobs=int(input("Enter the number of jobs:"))
    for _ in range(number_of_jobs):
        start_time=int(input("Emter the start time:"))
        finish_time=int(input("Enter the finiish time:"))
        value=int(input("Enter the value:"))
        jobs.append((start_time,finish_time,value))
    return jobs
jobs=get_jobs_from_user()
max_value,selected_jobs=weighted_interval_scheduling(jobs)
print("Maximum value:",max_value)
print("Selected jobs:")
for job in selected_jobs:
    print(f"Start time:{job[0]}, Finish Time:{job[1]} ,Value:{job[2]} ")
