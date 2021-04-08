function showprocess(){
    document.getElementById('fcfs').innerHTML = `<form action="/fcfs" method="POST" >
    <label for="name">Write Down the Name Of Process: </label><br>
<input type="text" style="margin:5px;background-color:rgb(35, 27, 54);border:0.3em solid #FFFFFF;margin:0 0.8em 0.8em 0;border-radius:2em;box-sizing: border-box; color:#FFFFFF" name="name" id="name"><br>
<label for="atime">Write down the values of Arrival Time with space separated: </label><br>
<input type="text" style="margin:5px;background-color:rgb(35, 27, 54);border:0.3em solid #FFFFFF;margin:0 0.8em 0.8em 0;border-radius:2em;box-sizing: border-box; color:#FFFFFF" name="atime" id="atime"><br>
<label for="etime">Write down the values of Execution Time/Burst Time with space separated: </label><br>
<input type="text" style="margin:5px;background-color:rgb(35, 27, 54);border:0.3em solid #FFFFFF;margin:0 0.8em 0.8em 0;border-radius:2em;box-sizing: border-box; color:#FFFFFF" name="etime" id="etime"><br>
<input type="submit" class="s1" value="Submit" >
</form>`
}
function sf(){
    document.getElementById('fcfs').innerHTML = `<form action="/shortestjobscheduling" method="POST" >
    <label for="name">Write Down the Name Of Process: </label><br>
<input type="text" style="margin:5px;background-color:rgb(35, 27, 54);border:0.3em solid #FFFFFF;margin:0 0.8em 0.8em 0;border-radius:2em;box-sizing: border-box; color:#FFFFFF" name="name" id="name"><br>
<label for="atime">Write down the values of Arrival Time with space separated: </label><br>
<input type="text" style="margin:5px;background-color:rgb(35, 27, 54);border:0.3em solid #FFFFFF;margin:0 0.8em 0.8em 0;border-radius:2em;box-sizing: border-box; color:#FFFFFF" name="atime" id="atime"><br>
<label for="etime">Write down the values of Execution Time/Burst Time with space separated: </label><br>
<input type="text" style="margin:5px;background-color:rgb(35, 27, 54);border:0.3em solid #FFFFFF;margin:0 0.8em 0.8em 0;border-radius:2em;box-sizing: border-box; color:#FFFFFF" name="etime" id="etime"><br>
<input type="submit" class="s1" value="Submit" >
</form>`
}
function rr(){
    document.getElementById('fcfs').innerHTML = `<form action="/roundrobin" method="POST" >
    <label for="name">Write Down the Name Of Process: </label><br>
<input type="text" style="margin:5px;background-color:rgb(35, 27, 54);border:0.3em solid #FFFFFF;margin:0 0.8em 0.8em 0;border-radius:2em;box-sizing: border-box; color:#FFFFFF" name="name" id="name"><br>
<label for="atime">Write down the values of Arrival Time with space separated: </label><br>
<input type="text" style="margin:5px;background-color:rgb(35, 27, 54);border:0.3em solid #FFFFFF;margin:0 0.8em 0.8em 0;border-radius:2em;box-sizing: border-box; color:#FFFFFF" name="atime" id="atime"><br>
<label for="etime">Write down the values of Execution Time/Burst Time with space separated: </label><br>
<input type="text" style="margin:5px;background-color:rgb(35, 27, 54);border:0.3em solid #FFFFFF;margin:0 0.8em 0.8em 0;border-radius:2em;box-sizing: border-box; color:#FFFFFF" name="etime" id="etime"><br>
<label for="qt">Write quantum time: </label><br>
<input type="text" style="margin:5px;background-color:rgb(35, 27, 54);border:0.3em solid #FFFFFF;margin:0 0.8em 0.8em 0;border-radius:2em;box-sizing: border-box; color:#FFFFFF" name="qt" id="qt"><br>
<input type="submit" class="s1" value="Submit" >
</form>`
}

