from django.shortcuts import render
from django.db.models import Q
from .models import dialogue, QA
from datetime import datetime
import csv


def index(request):

    question = None

    try:
        question = request.POST["question"]
        dialogue.objects.create(
            message = question,
            send_bot = False,
            send_date = datetime.now(),
        )
       
    except:
        pass
   
    
    if  QA.objects.filter(user_input = request.POST.get("question", False)):
        answer_list = QA.objects.filter(user_input = request.POST.get("question", False))

        dialogue.objects.create(
            message = answer_list[0].bot_reply,
            send_bot = True,
            send_date = datetime.now(),
        )
    else:
        answer_list = QA.objects.all().filter(user_input__contains = request.POST.get("question", False))

        if len(answer_list) == 0:
            answer_none = "すみません。もう一度入力してください。"
        
            dialogue.objects.create(
                message = answer_none,
                send_bot = True,
                send_date = datetime.now(),
            )
        else:
            bot_first_word = "「" + request.POST["question"] + "」でよくある質問はこちらです。"
            
            dialogue.objects.create(
                message = bot_first_word,
                send_bot = True,
                send_date = datetime.now(),
            )

            bot_message =[]

            for i in range(len(answer_list)):
                bot_message.append("【質問" + str(i+1) + "】" + answer_list[i].user_input + "\r\n【回答】" + answer_list[i].bot_reply)

                dialogue.objects.create(
                    message = bot_message[i],
                    send_bot = True,
                    send_date = datetime.now(),
                ) 

           
    date_list = dialogue.objects.all()

    context = {
        "question": question,
        "date_list": date_list,
    }

    return render(request, "main/index.html", context)


with open('sample.csv', 'r') as f:
    render = csv.reader(f)
    for i in render:
        render_question.append(render[1])



# Create your views here.
