from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')


@app.route('/fcfs', methods=['POST'])

def fcfs():
    if request.method == 'POST':

        print("Write Down the Name Of Process ") 
        process_list=list(map(str,request.form['name'].split())) 
        print("Write down the values of Arrival Time with space separated") 
        arrival_time=list(map(float,request.form['atime'].split())) 
        print(arrival_time)
        print("Write down the values of Execution Time/Burst Time with space separated") 
        execution_time=list(map(float,request.form['etime'].split())) 
        dict1=list(zip(process_list,arrival_time,execution_time)) 
        l=len(dict1) 
        dict1_1=dict1
        for i in range(0,l): 
            for j in range(0,l-i-1): 
                if(dict1[j][1]>dict1[j+1][1]): 
                    tempo=dict1[j] 
                    dict1[j]=dict1[j+1] 
                    dict1[j+1]=tempo
        pid = []
        dict1_2= dict1 
        completion_time=[]
        k=0 
        at = []
        bt = []
        for i,j,k in dict1:
            pid.append("p"+str(i))
            at.append(j)
            bt.append(k)
        p=0
        main_list = []
        rt = []
        for i in range(len(at)):
            list_ = []
            if i==0:
                list_.append(at[i])
                rt.append(at[i]-at[i])
                list_.append(at[i]+bt[i])
                completion_time.append(at[i]+bt[i])
                p = at[i]+bt[i]
                main_list.append(list_)
            else:
                if at[i]<bt[i-1]:
                    list_.append(p)
                    rt.append(p-at[i])
                    list_.append(p+bt[i])
                    completion_time.append(p+bt[i])
                    p = p+bt[i]
                elif at[i]>=bt[i-1] and not(at[i]<p):
                    list_.append(at[i])
                    rt.append(at[i]-at[i])
                    list_.append(at[i]+bt[i])
                    completion_time.append(at[i]+bt[i])
                    p = at[i]+bt[i]
                elif at[i]<p:
                    list_.append(p)
                    rt.append(p-at[i])
                    list_.append(p+bt[i])
                    completion_time.append(p+bt[i])
                    p = p+bt[i]
                main_list.append(list_)
        tt = []
        zip_turn = zip(completion_time,at)
        for i,j in zip_turn:
            tt.append(i-j)
        wt = []
        zip_turn_2 = zip(tt,bt)
        for i,j in zip_turn_2:
            wt.append(i-j)
        dict2=list(zip(pid,main_list))
        avg_turnaround_time = sum(tt)/len(at)
        avg_waiting_time = sum(wt)/len(at)
        avg_response_time = sum(rt)/len(at)
        ideal_time=0
        for items in range(len(main_list)):
            if items!=0:
                ideal_time += main_list[items][0]-main_list[items-1][1]
        cpu_utilization = round(((int(main_list[-1][1]) - ideal_time)/main_list[-1][1])*100,2)
        return render_template('fcfs.html',dict1_1=dict1_1,dict1_2=dict1_2,dict2=dict2 , main_list=main_list, completion_time=completion_time,tt=tt,wt=wt,rt=rt,att=avg_turnaround_time,awt=avg_waiting_time,art=avg_response_time)

@app.route('/shortestjobscheduling', methods=['POST'])

def shortestjobscheduling():
    if request.method == 'POST':
        print("Write Down the Name Of Process ") 
        process_list=list(map(str,request.form['name'].split())) 
        print("Write down the values of Arrival Time with space separated") 
        arrival_time=list(map(float,request.form['atime'].split())) 
        print(arrival_time)
        print("Write down the values of Execution Time/Burst Time with space separated") 
        execution_time=list(map(float,request.form['etime'].split()))  
        dict1=list(zip(process_list,arrival_time,execution_time)) 
        l=len(dict1) 
        dict1_1=dict1
        dict1_2= dict1
        
        pid=[]
        k=0 
        at = []
        bt = []
        for i,j,k in dict1:
            pid.append(i)
            at.append(j)
            bt.append(k)
        
        avg_turnaround_time =0.0
        avg_waiting_time=0.0
        avg_response_time=0.0
        cpu_utilisation=0.0
        total_turnaround_time = 0
        total_waiting_time = 0
        total_response_time = 0
        total_idle_time = 0
        is_completed=[0]*100
        current_time = 0
        completed = 0
        prev = 0
        start_time=[0]*len(at)
        tt=[0]*len(at)
        wt=[0]*len(at)
        rt=[0]*len(at)
        completion_time=[0]*len(at)


        while(completed != len(at)):
            idx = -1
            mn = 10000000
            for i in range(len(at)):
                if(at[i] <= current_time and is_completed[i] == 0):
                    if(bt[i] < mn):
                        mn = bt[i]
                        idx = i
                    if(bt[i] == mn):
                        if(at[i] < at[idx]):
                            mn = bt[i]
                            idx = i
            if idx!=-1:
                start_time[idx] = current_time
                completion_time[idx] = start_time[idx] + bt[idx]
                tt[idx] = completion_time[idx] - at[idx]
                wt[idx] = tt[idx] - bt[idx]
                rt[idx] = start_time[idx] - at[idx]

                total_turnaround_time += tt[idx]
                total_waiting_time += wt[idx]
                total_response_time += rt[idx]
                total_idle_time += start_time[idx] - prev

                is_completed[idx] = 1
                completed=completed+1
                current_time = completion_time[idx]
                prev = current_time
            else:
                current_time=current_time+1
        min_arrival_time = 10000000
        max_completion_time = -1
        for i in range(len(at)):
            min_arrival_time = min(min_arrival_time,at[i])
            max_completion_time = max(max_completion_time,completion_time[i])

        avg_turnaround_time = total_turnaround_time / len(at)
        avg_waiting_time = total_waiting_time / len(at)
        avg_response_time = total_response_time / len(at)
        cpu_utilization = ((max_completion_time - total_idle_time) / max_completion_time )*100
        
        pid_new=[]
        for i in range(0,l): 
            for j in range(0,l-i-1): 
                if(dict1[j][2]>dict1[j+1][2]): 
                    tempo=dict1[j] 
                    dict1[j]=dict1[j+1] 
                    dict1[j+1]=tempo
        for i,j,k in dict1:
            pid_new.append("p"+str(i))
        dict2=list(zip(pid_new))
        return render_template('sjf.html',dict1_1=dict1_1,dict1_2=dict1_2,dict2=dict2 ,tt=tt,wt=wt,rt=rt,att=avg_turnaround_time,awt=avg_waiting_time,art=avg_response_time,)

@app.route('/roundrobin', methods=['POST'])

def roundrobin():
    if request.method == 'POST':
        print("Write Down the Name Of Process ") 
        process_list=list(map(str,request.form['name'].split())) 
        print("Write down the values of Arrival Time with space separated") 
        arrival_time=list(map(float,request.form['atime'].split())) 
        print(arrival_time)
        print("Write down the values of Execution Time/Burst Time with space separated") 
        execution_time=list(map(float,request.form['etime'].split()))  
        print("Write quantum time: ")
        q = int(request.form['qt'])
        dict3=list(zip(process_list,arrival_time,execution_time)) 
        l=len(dict3) 
        print(dict3)
        for i in range(0,l): 
            for j in range(0,l-i-1): 
                if(dict3[j][1]>dict3[j+1][1]): 
                    tempo=dict3[j] 
                    dict3[j]=dict3[j+1] 
                    dict3[j+1]=tempo
        pid = []
        
        p=len(dict3)
        dict1_1=dict3
        dict1_2= dict3
        N = p #rows
        M = 4 #columns
        a = [ [ 0 for i in range(M) ] for j in range(N) ]
        M1 = 5
        b = [ [ 0 for i in range(M1) ] for j in range(N) ]
        t=0
        at = []
        bt = []
        for i,j,k in dict3:
            pid.append(int(i))
            at.append(int(j))
            bt.append(int(k))
        for i,j,k in dict3:
            a[t][0] = int(i)
            a[t][1] = int(j)
            a[t][2] = int(k)
            a[t][3] = int(k)
            t=t+1
        k=0
        h=0
        s=0
        idle=0
        done=0
        sum_=0.0
        final=[]
        i=a[0][1]
        dict_={}

        while(done!=p):
            if(k==p):
                k=0
            if(a[k][1]<=i):
                if(a[k][2]!=0):
                    if(a[k][2]>=q):
                        final.append(i)
                        final.append("p"+str(a[k][0]))
                        a[k][2]-=q
                        i+=q
                    else:
                        final.append(i)
                        final.append("p"+str(a[k][0]))
                        i+=a[k][2]
                        a[k][2]=0
                    if(a[k][2]==0):
                        b[s][0]=a[k][0]
                        b[s][1]=a[k][1]
                        b[s][2]=i
                        b[s][3]=a[k][3]
                        b[s][4]=((i-a[k][1])-a[k][3]) 
                        sum_+=((i-a[k][1])-a[k][3])
                        s=s+1
                        done=done+1

                    idle=0
                k=k+1
            else:
                if(idle==0):
                    idle=1
                    k=0
                elif(idle==1):
                    final.append(i)
                    final.append("Idle")
                    idle=2
                    i=i+1   
                else:
                    i=i+1

        final.append(i)
        chart=[]
        dict1={}
        dict2={}
        ideal_time=0
        timeline=[]
        for k in range(len(final)-2):
            if k==0:
                new = final[k:k+3]

                chart.append(new[1])
            elif isinstance(final[k],int):
                new=final[k:k+3]
                chart.append(new[1])
  
            if isinstance(new[1],str) and new[1]!="Idle":
                dict1[new[1]]=new[2]
                if new[1] not in dict2.keys():
                    dict2[new[1]]=new[0]
        for k in range(len(final)-2):
            if isinstance(final[k:k+3][1],str) and final[k:k+3][1]=="Idle":
                ideal_time+=final[k:k+3][2]-final[k:k+3][0]
            
        
        st=list(dict2.values())
        et=list(dict1.values())
        
        for k in range(len(final)):
            if isinstance(final[k],int):
                timeline.append(final[k])
        utilization = (timeline[-1]-ideal_time)/timeline[-1]
        cpu_utilization = round(utilization*100,2)
        tt=[]
        wt=[]
        rt=[]
        for i in range(p):
            tt.append(et[i]-at[i])
        for i in range(p):
            wt.append(tt[i]-bt[i])
        for i in range(p):
            rt.append(st[i]-at[i])
        avg_turnaround_time = sum(tt)/p
        avg_waiting_time = sum(wt)/p
        avg_response_time = sum(rt)/p

        dict2=list(zip(chart))
        return render_template('rr.html',dict1_1=dict1_1,dict1_2=dict1_2,dict2=dict2 ,tt=tt,wt=wt,rt=rt,att=avg_turnaround_time,awt=avg_waiting_time,art=avg_response_time)


if __name__ == "__main__":
    app.run()
