def todo_top():
    result = '''
<!doctype html>
<!--html 주석-->
<!--x 위에 하얀 박스 올려두고, hover로 하얀박스 display:none 하면-->
<html>
<head>
<meta charset="utf-8">
<title>To do list</title>
<style>
	/*html과 body의 height를 정해야 이를 기준으로 height n% 가 적용됨
	  %는 상대적인 값인데, 기준으로삼을 상위 태그의 height 값이 없으면 적용되지 않을 수 있음*/
	html{height:100%}
	body{
		background-color:#D9D9D9;
		height:100%;
		margin:0;
		padding:0;
	}
	.wrap{
		position:absolute;
		left:50%;
		transform:translateX(-50%);
		background-color:#FFFFFF;
		width:900px;
		height:100%;
		margin:0 auto;
		overflow-y:auto;
		overflow-x:hidden;
	}
	.add{
		background:#ffffff;
		width:780px;
		height:50px;
		float:center;
		margin:0px 60px;
		border:#D9D9D9 dashed;
		border-radius:10px;
		text-align:center;
		font-size:30px;
		color:#D9D9D9;
		font-weight:bold;
		cursor:pointer;
	}
	#add{
                display:none;
		margin:-2px 60px;
		padding:4px 10px;
		width:760px;
		align:center;
		border-radius:5px;
	}
	div > input{
		position:relative;
		width:80%;
		padding-left:15px;
		background:#F0F0F0;
		box-shadow:1px 1px 2px 1px #D0D0D0 inset;
		border:none;
		height:35px;
		margin:2px 15px;
		border-radius:10px;
	}
	.submit{
		background:#F0F0F0;
		width:80px;
		height:115px;
		position:absolute;
		top:155px;
		right:80px;
		border:#F0F0F0;
		box-shadow:1px 1px 2px 1px #D0D0D0;
		border-radius:10px;
		font-size:20px;
		color:#606060;
		cursor:pointer;
	}
	.todo {
		width:780px;
		height:45px;
		position:relative;
		flat:center;
		margin:10px 60px 0px 60px;
		border:3px #D9D9D9 solid;
		border-radius:10px;
		/*cursor:pointer;*/
	}
	.before{background:#FFFFFF;}
	.after{background:#D9D9D9;}
	.todo > .title{
		font-size:23px;
		font-weight:bold;
		position:absolute;
		top:7px;
		left:45px;
		cursor:pointer;
	}
	.todo > .duedate{
		font-size:14px;
		color:#828282;
		font-weight:bold;
		position:absolute;
		top:13px;
		right:13px;
	}
	.todo > .del{
		background:url(images/del.png) no-repeat;
		position:absolute;
		border:none;
		background-size:18px;
		width:18px;
		height:18px;
		top:15px;
		right:-30px;
		cursor:pointer;
	}

	.dead{
		background:#FFC000;
		border:#FFC000 solid;
	}
	.dead > .title{color:white;}
	.dead > .duedate{color:white;}
	.done{
		background:white;
	}
	.done > .title{
		color:#D9D9D9;
		text-decoration:line-through;
	}
	.done > .duedate{
		color:#D9D9D9;
	}
	.content{
		display:none;
		width:700px;
		border:#D9D9D9 solid;
		border-width:5px;
		border-top:0px;
		border-right:0px;
		border-bottom:0px;
		margin:-2px 80px;
		padding:5px 10px;
		
	}
	.done + .content{
		color:#D9D9D9;
	}
	.dead + .content{
		border:#FFC000 solid;
		border-width:5px;
		border-top:0px;
		border-right:0px;
		border-bottom:0px;
	}

	.edit{
		position:absolute;
		right:75px;
		background:url("images/edit.png") no-repeat;
		background-size:30px;
		border:none;
		width:30px;
		height:30px;
		cursor:pointer;
	}
	.noti{
		/*display:none; //notification도 이벤트처리*/
		background:url(images/notification.png) no-repeat;
		position:absolute;
		border:none;
		background-size:320px;
		width:320px;
		height:80px;
		top:10px;
		right:-2px;
		cursor:pointer;
	}
	input[id^="ch"]{display:none;}
	input[id^="ch"] + label{
		position:absolute;
		left:6px;
		top:8px;
		display:inline-block;
		background:url("images/unchecked.png") no-repeat;
		background-size:30px;
		width:30px;
		height:30px;
		cursor:pointer;
	}
	input[id^="ch"]:checked + label{
		background:url("images/checked.png") no-repeat;
		background-size:30px;
		width:30px;
		height:30px;
	}

	
</style>
<script src="//code.jquery.com/jquery-1.10.2.js"></script>
<script src="//code.jquery.com/ui/1.11.4/jquery-ui.js"></script>
<script src="http://code.jquery.com/jquery-latest.js"></script>	
<script>
	var gbl_idx;
	$.ajax({
		url:"/get_idx",
		dataType : "json",
		success:function(data){
                        //alert(data.idx);
			gbl_idx=data.idx;
		}
	});
	$(document).ready(function(){
		var Now = new Date();
		var today = Now.getFullYear();
		today += "-"+("00"+(Now.getMonth()+1)).slice(-2);
		today += "-"+Now.getDate();
	//alert(typeof($("#duedate").attr("id")));
		$("#duedate").attr("min",today);
		$(".title").click(function(){
			//del 누르면 바로 삭제가 가능하면(변화 보이지 않고)
			//var todo_id = $(this)attr("id")
			var todo_id = $(this).parent().attr("id")
			$("#show"+todo_id).toggle();
			$("#"+todo_id).toggleClass("after before");
		});
		$(".add").click(function(){
			$("#add").toggle();
		});
		$("input").click(function(){
			if($(this).attr("type")=="checkbox"){
			var todo_id = $(this).parent().attr("id")
			if($(this).parent().hasClass("dead")==true){
				$("#"+todo_id).css("display","none");
			}
			$("#"+todo_id).toggleClass("done");
			$.ajax({
				url:"/check",
				type:"POST",
				data:todo_id+"-check"
			});
			}
		});
		$(".submit").click(function(){
                        $("#add").toggle();
			gbl_idx += 1;
			var title = $('input[name=title]').val();
			var content = $('input[name=content]').val();
			var duedate = $('input[name=duedate]').val();
			var d = gbl_idx+","+title+","+content+","+duedate+",-1"
			$.ajax({
				url:"/add",
				type:"POST",
				data:d,
				//success:function(){alert("success");}
			});
			$('input[name=title]').val('');
			$('input[name=content]').val('');
			$('input[name=duedate]').val('');
		})
		$(".del").click(function(){
                        var todo_id = $(this).parent().attr("id")
                        $.ajax({
                                url:"/delete",
                                type:"POST",
                                data:todo_id,
                        });
                });

	});

	
</script>
</head>

<body>

<div class="wrap">
	<a href="/todo">
		<img src="images/todolist.png" width="340" alt="to do list">
	</a>
	<button class="noti"></button>
	<div>	
	  <button class="add"> + </button>
		<div id="add">
			<input type="text" name="title" placeholder="to do title"><br>
			<input type="text" name="content" placeholder="to do content"><br>
			<input type="date" id="duedate" name="duedate" min="2019-05-17"><br>
			<button class="submit"> ADD </button>
		</div>
	</div>

	'''
    return result



def new_todo(data):
    idx = data[0]
    title = data[1]
    content = data[2]
    done = data[3]
    duedate = data[4]
    
    result = '''
	<div id="%d" class="todo before">
		<input type="checkbox" id="ch%d">
		<label for="ch%d"></label>
		<div class="title"> %s</div>
		<div class="duedate">%s 마감</div>
		<div class="del"></div>
	</div>
	<div id="show%d" class="content">
                %s<button class="edit"></button><br><br>
	</div>
	'''%(idx, idx,idx,title, duedate, idx, content)
    
    if done:
        result = result.replace("todo before", "todo before done")
    
    return result

def todo_bottom():
    result = '''
	<br>
</div>

</body>
</html>
'''
    return result


def dead_top():
    result = todo_top()[:-103]
    return result

def dead_todo(data):
    idx = data[0]
    title = data[1]
    content = data[2]
    done = data[3]
    duedate = data[4]
    
    result = '''
	<div id="%d" class="todo before dead">
		<input type="checkbox" id="ch%d">
		<label for="ch%d"></label>
		<div class="title"> %s</div>
		<div class="duedate">%s 마감</div>
		<div class="del"></div>
	</div>
	<div id="show%d" class="content">
                %s<button class="edit"></button><br><br>
	</div>
	'''%(idx, idx,idx,title, duedate, idx, content)
    return result

    
